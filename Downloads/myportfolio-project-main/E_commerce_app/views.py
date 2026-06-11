from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category




def ecom_homepage(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_featured=True)[:8]
    context = {
        'categories': categories,
        'featured_products': featured_products
    }
    return render(request, 'ecom_app/ecom_homepage.html', context)


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
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'ecom_app/product_detail.html', context)
