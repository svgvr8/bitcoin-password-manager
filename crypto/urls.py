from django.urls import path
from . import models, forms
from .views import encrypt_view, decrypt_view

urlpatterns = [
    path('encrypt/', encrypt_view, name='encrypt'),
    path('decrypt/', decrypt_view, name='decrypt'),
]
