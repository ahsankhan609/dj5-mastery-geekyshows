from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime

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


def home(request):

    # Django By-Default Templates - showing how to display variables

    greetings = "Hello, Good Morning"  # passing variable to context
    country = "USA"  # passing variable to context
    designation = "python developer"  # passing variable to context
    guest_names = {
        'guest1': 'John',
        'guest2': 'Jane',
        'guest3': 'Joe',
        'greetings': greetings,
        'country': country,
        'designation': designation,
        'description': 'We are python developer\'s. We live in USA.',
        'age': 0,
        'dt': datetime.now(),
        # passing list to context
        'linux_distros': ['CentOS', 'Debian', 'Fedora', 'Ubuntu'],
    }

    # Django By-Default Templates - showing how to use Filters

    return render(request, 'challenges/index.html', context=guest_names)
