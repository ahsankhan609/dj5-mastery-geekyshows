from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the challenges index.")


def requested_month_by_number(request, month):
    return HttpResponse(f"<h1>{month}</h1>")


def requested_month(request, month):
    challenge_month = None

    if month == "january" or month == "jan":
        challenge_month = "This is the month of January."
    elif month == "february" or month == "feb":
        challenge_month = "This is the month of February."
    elif month == "march" or month == "mar":
        challenge_month = "This is the month of March."
    else:
        return HttpResponseNotFound("<h1>Month not Supported.</h1>")

    return HttpResponse(f"<h1>{challenge_month}</h1>")
