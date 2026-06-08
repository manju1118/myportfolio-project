from django.urls import path
from . import views




urlpatterns = [
    path('', views.blog_homepage, name='blog_homepage'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.blog_create, name='blog_create'),
]
