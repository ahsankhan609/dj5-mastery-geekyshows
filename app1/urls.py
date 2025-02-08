# myapp/urls.py
from django.urls import path
from .views import index, about

app_name = 'app1'  # Setting a namespace
urlpatterns = [
    path('', index, name='app1-home'),  # Route for home page
    path('about/', about, name='app1-about'),  # Route for about page
]
