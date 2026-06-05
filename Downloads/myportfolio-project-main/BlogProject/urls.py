from django.urls import path
from . import views





urlpatterns = [
    path('blog/blog_homepage/', views.blog_homepage, name='blog_homepage'),
    path('blog/category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('blog/post/<slug:slug>/', views.post_detail, name='post_detail'),
]