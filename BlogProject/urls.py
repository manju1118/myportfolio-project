from django.urls import path
from . import views





urlpatterns = [
    path('blog/blog_homepage/', views.blog_homepage, name='blog_homepage'),
]