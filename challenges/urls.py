# myapp/urls.py
from django.urls import path
from .views import index

app_name = 'challenges'  # Setting a namespace
urlpatterns = [
    path('', index, name='homepage'),  # Route for home page
]
