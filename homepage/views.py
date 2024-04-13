from django.shortcuts import render
from django.http import HttpResponse
from galleries.models import Image


def home_view(request):
    images = Image.objects.all()

    if request.htmx:
        return render(request, "home_partial.html", {"images": images})
    return render(request, "home.html", {"images": images})


