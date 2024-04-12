from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    if request.htmx:
        return render(request, "home_partial.html")
    return render(request, "home.html")


