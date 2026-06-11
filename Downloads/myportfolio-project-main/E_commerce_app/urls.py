from django.urls import path
from . import views




urlpatterns = [
    path('', views.ecom_homepage, name='ecom_homepage'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]
