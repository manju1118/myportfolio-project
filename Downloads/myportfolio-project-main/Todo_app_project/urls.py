from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_homepage, name='todo_homepage'),
    path('create-todo/', views.create_todo, name='create_todo'),
    path('complete-todo/<int:id>/', views.complete_todo, name='complete_todo'),
    path('delete-todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('update-todo/<int:id>/', views.update_todo, name='update_todo'),
   
    path('dashboard/', views.todo_dashboard, name='todo_dashboard'),
]