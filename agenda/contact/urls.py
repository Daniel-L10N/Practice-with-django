from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='contact'),
    path('view/<int:id>', view , name='contact_view'),
    path('edit/<int:id>', edit, name="contact_edit")
]
