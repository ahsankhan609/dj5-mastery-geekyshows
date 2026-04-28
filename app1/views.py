from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the app1 index.")


def about(request) -> HttpResponse:
    return HttpResponse("I am a python developer.From app1")
