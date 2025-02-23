from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="todo_index"),
    path('delete/<str:items_id>', remove, name='delete')
]
