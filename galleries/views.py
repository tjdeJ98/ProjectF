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
        return render(request, "galleries_partial.html", {"images": images})
    return render(request, "galleries.html", {"images": images})
