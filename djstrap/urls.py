# myapp/urls.py
from django.urls import path
from .views import *

app_name = 'djstrap'  # Setting a namespace

urlpatterns = [
    path('', index, name='homepage'),  # Route for home page
]
