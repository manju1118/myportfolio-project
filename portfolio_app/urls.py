from django.urls import path
from . import views




urlpatterns = [
    path('', views.homepage, name='homepage'),
    path(
        'portfolio/about_page/', views.about_page,name='about'
    ),
    path(
        'portfolio/services/', views.services,name='services'
    ),
    path('portfolio/projects/', views.projects, name='projects'),
    path('portfolio/contact/', views.contact, name='contact'),
    path('projects/blog-platform/', views.blog_project, name='blog_project'),
]