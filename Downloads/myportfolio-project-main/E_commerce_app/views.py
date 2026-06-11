from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Cart, Order, Wishlist, Review
from django.db.models import Q
from django.contrib import messages
from django.db.models import Avg
import razorpay
from django.conf import settings



def ecom_homepage(request):

    query = request.GET.get('query')
    sort = request.GET.get('sort')

    categories = Category.objects.all()

    featured_products = Product.objects.filter(
        is_featured=True
    )[:8]

    product = Product.objects.all()

    if query:

        product = product.filter(

            Q(title__icontains=query) |

            Q(description__icontains=query) |

            Q(category__name__icontains=query)

        )

    if sort == 'low':

        product = product.order_by(
            'price'
        )

    elif sort == 'high':

        product = product.order_by(
            '-price'
        )
    elif sort == 'latest':
        product = product.order_by(
            '-created_at'
        )

    context = {

        'categories': categories,

        'featured_products': featured_products,

        'product': product,

        'query': query,

        'sort': sort

    }

    return render(
        request,
        'ecom_app/ecom_homepage.html',
        context
    )


def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'ecom_app/category_products.html', context)

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.filter(
        category=product.category).exclude(id=product.id)[:4]
    reviews = product.reviews.all().order_by(
        '-created_at'
    )

    average_rating = product.reviews.aggregate(
        Avg('rating')
    )['rating__avg']
    context = {
        'product': product,
        'related_products': related_products,
        'reviews':reviews,
        'average_rating':average_rating
    }
    return render(request, 'ecom_app/product_detail.html', context)


#cart views

@login_required
def add_to_cart(request, slug):
    product = Product.objects.get(slug=slug)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity +=1
        cart_item.save()

    messages.success(
        request,
        "Product added to cart"
    )
    return redirect(
        'product_detail',
        slug=slug
    )

@login_required
def cart_page(request):

    cart_items = Cart.objects.filter(

        user=request.user

    )

    total_price = 0

    for item in cart_items:

        total_price += (

            item.product.price *

            item.quantity

        )

    context = {

        'cart_items': cart_items,

        'total_price': total_price

    }

    return render(

        request,

        'ecom_app/cart_page.html',

        context

    )

@login_required
def remove_cart_item(request, id):

    item = Cart.objects.get(
        id=id,
        user=request.user
    )

    item.delete()

    return redirect(
        'cart_page'
    )

@login_required
def checkout(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total_price = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    if request.method == 'POST':

        Order.objects.create(

            user=request.user,

            full_name=request.POST.get(
                'full_name'
            ),

            phone=request.POST.get(
                'phone'
            ),

            address=request.POST.get(
                'address'
            ),

            total_price=total_price,

            status='Pending'

        )

        cart_items.delete()

        messages.success(
            request,
            "Order placed successfully 🎉"
        )

        return redirect(
            'orders'
        )

    return render(
        request,
        'ecom_app/checkout.html',
        {
            'cart_items': cart_items,
            'total_price': total_price
        }
    )


@login_required
def orders(request):

    orders = Order.objects.filter(

        user=request.user

    ).order_by(

        '-created_at'

    )

    return render(

        request,

        'ecom_app/orders.html',

        {

            'orders': orders

        }

    )

@login_required
def add_to_wishlist(request, slug):

    product = Product.objects.get(
        slug=slug
    )

    Wishlist.objects.get_or_create(

        user=request.user,

        product=product

    )

    messages.success(
        request,
        "Added to wishlist ❤️"
    )

    return redirect(
        'product_detail',
        slug=slug
    )

@login_required
def remove_wishlist(request, id):

    wishlist = Wishlist.objects.get(
        id=id,
        user=request.user
    )

    wishlist.delete()

    messages.success(
        request,
        "Removed from wishlist"
    )

    return redirect(
        'wishlist_page'
    )


@login_required
def wishlist_page(request):

    wishlist_items = Wishlist.objects.filter(

        user=request.user

    ).order_by(

        '-created_at'

    )

    return render(

        request,

        'ecom_app/wishlist.html',

        {

            'wishlist_items': wishlist_items

        }

    )

@login_required
def add_review(request, slug):

    product = Product.objects.get(
        slug=slug
    )

    if request.method == 'POST':

        rating = request.POST.get(
            'rating'
        )

        comment = request.POST.get(
            'comment'
        )

        Review.objects.create(

            product=product,

            user=request.user,

            rating=rating,

            comment=comment

        )

    return redirect(
        'product_detail',
        slug=slug
    )

@login_required
def payment_success(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total_price = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    Order.objects.create(

        user=request.user,

        full_name=request.POST.get(
            'full_name'
        ),

        phone=request.POST.get(
            'phone'
        ),

        address=request.POST.get(
            'address'
        ),

        total_price=total_price

    )

    cart_items.delete()

    return redirect(
        'orders'
    )