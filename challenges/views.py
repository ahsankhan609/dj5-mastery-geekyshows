from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from datetime import datetime
from typing import Any

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the challenges index.")


def requested_month_by_number(request: HttpRequest, month: int) -> HttpResponse:
    """
    Description:
        return Number on the basis of month number provided in the URL.
    Example:
    http://127.0.0.1:8000/challenges/12
    """
    return HttpResponse(f"<h1>{month}</h1>")


def requested_month(request: HttpRequest, month: str) -> HttpResponseNotFound | HttpResponse:
    """
    Description:
        return string on the basis of month name provided in the URL.
    Example:
    http://127.0.0.1:8000/challenges/jan
    http://127.0.0.1:8000/challenges/march
    """
    try:
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
    except Exception as e:
        return HttpResponseNotFound(f"<h1>Error: {str(e)}</h1>")


def home(request: HttpRequest) -> HttpResponse:
    """
    Description:- Django By-Default Templates - showing how to display variables on the HTML template
    Example:- http://127.0.0.1:8000/challenges/home/
    """

    # Django By-Default Templates - showing how to display variables

    greetings: str = "Hello, Good Morning"  # passing variable to context
    country: str = "USA"  # passing variable to context
    designation: str = "python developer"  # passing variable to context
    guest_names: dict[str, Any] = {
        'guest1': 'John',
        'guest2': 'Jane',
        'guest3': 'Joe',
        'greetings': greetings,
        'country': country,
        'designation': designation,
        'description': 'We are python developer\'s. We live in USA.',
        'age': 50,
        'dt': datetime.now(),
        # passing list to context
        'linux_distros': ['CentOS', 'Debian', 'Fedora', 'Ubuntu'],
    }

    # Django By-Default Templates - showing how to use Filters

    return render(request, 'challenges/index.html', context=guest_names)
