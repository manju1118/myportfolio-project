from django.urls import path
from . import views




urlpatterns = [
    path('', views.ecom_homepage, name='ecom_homepage'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path(
        'add-to-cart/<slug:slug>/',
        views.add_to_cart,
        name='add_to_cart'
    ),
    path('cart/',views.cart_page,name='cart_page'),
    path(
    'remove-cart-item/<int:id>/',
    views.remove_cart_item,
    name='remove_cart_item'
    ),
    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),
    path(
    'orders/',
    views.orders,
    name='orders'
    ),
    path(
    'wishlist/<slug:slug>/',
    views.add_to_wishlist,
    name='add_to_wishlist'
    ),
    path(
    'wishlist/remove/<int:id>/',
    views.remove_wishlist,
    name='remove_wishlist'
    ),
    path(
    'wishlist/',
    views.wishlist_page,
    name='wishlist_page'
    ),
    path(
    'review/<slug:slug>/',
    views.add_review,
    name='add_review'
    ),
    path(
    'payment-success/',
    views.payment_success,
    name='payment_success'
    ),
]
