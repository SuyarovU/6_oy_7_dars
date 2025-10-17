from django.urls import path
from .views import index, create_todo, todo_item, delete, edit

urlpatterns = [
    path('', index, name="home"),
    path('create/', create_todo, name="todo_create"),
    path('todos/<int:pk>', todo_item, name="todo_item"),
    path('delete/<int:pk>', delete, name="delete"),
    path('edit/<int:pk>', edit, name="edit")
]
