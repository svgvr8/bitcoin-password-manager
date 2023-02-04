from django.urls import path
from . import views

app_name = 'crypto'

urlpatterns = [
    path('encrypt/', views.encrypt, name='encrypt'),
    path('decrypt/', views.decrypt, name='decrypt'),
]
