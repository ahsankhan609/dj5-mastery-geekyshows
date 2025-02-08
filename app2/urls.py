# myapp/urls.py
from django.urls import path
from .views import index, about

app_name = 'app2'  # Setting a namespace
urlpatterns = [
    path('', index, name='app2-home'),  # Route for home page
    path('about/', about, name='app2-about'),  # Route for about page
]
