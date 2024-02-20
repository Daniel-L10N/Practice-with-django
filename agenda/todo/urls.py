from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='todo'),
    path('view/<int:id>', view, name='todo_view'),
    path('edit/<int:id>', edit, name='todo_edit'),
    path('create/', create, name='todo_create'),
    path('delete/<int:id>', delete, name='todo_delete'),
]
