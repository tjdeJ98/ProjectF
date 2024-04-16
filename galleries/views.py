from django.shortcuts import render
from os import listdir
from pathlib import Path
from django.conf import settings
from galleries.models import Image
# Create your views here.


def galleries(request):
    images = Image.objects.all()
    # TODO: get image paths from the db

    if request.htmx:
        return render(request, "galleries_partial.html")
    return render(request, "galleries.html", {"page": "galleries_partial.html"} )


def plants(request):
    images = Image.objects.all()

    if request.htmx:
        return render(request, "plants_gal.html", {"images": images})
    # TODO still need to send the images
    return render(request, "galleries.html", {"page": "plants_gal.html"})