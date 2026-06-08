from django.urls import path
from . import views




urlpatterns = [
    path('', views.blog_homepage, name='blog_homepage'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.blog_create, name='blog_create'),
    path(
    'post/update/<slug:slug>/',
    views.post_update,
    name='post_update'
    ),
    path(
    'post/delete/<slug:slug>/', views.post_delete, name='post_delete'),
    path('post/like/<slug:slug>/', views.like_post, name='like_post'),
    path('post/comment/<slug:slug>/', views.add_comment, name='add_comment'),

]
