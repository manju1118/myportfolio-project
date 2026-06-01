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
    path('projects/ecommerc_platform/', views.ecommerce_project,name='ecommerce_project'),
    path('projects/todo_management/',views.todo_management,name='todo_management'),
    path('projects/personal_system/',views.personal_system,name='personal_system'),
    path('projects/creative_portfolio/',views.creative_portfolio,name='creative_portfolio'),
    path('projects/',views.corporate_business,name='corporate_business'),
]