from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app2 index.")


def about(request):
    return HttpResponse("I am a python developer. From App2.")
