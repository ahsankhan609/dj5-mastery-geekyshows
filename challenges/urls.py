# myapp/urls.py
from django.urls import path
from .views import index, requested_month_by_number, requested_month

app_name = 'challenges'  # Setting a namespace
urlpatterns = [
    path('', index, name='homepage'),  # Route for home page
    path('<int:month>', requested_month_by_number, name='requested_month_by_number'),
    path('<str:month>', requested_month, name='requested_month'),
]
