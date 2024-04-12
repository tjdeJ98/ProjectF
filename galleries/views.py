from django.shortcuts import render
from os import listdir
from pathlib import Path
from django.conf import settings
from galleries.models import Image
# Create your views here.


def galleries(request):
    images = Image.objects.all()
    # TODO: get image paths from the db
    path = Path(r"theme\static\media\gallerie") # Wrong folder but works for now
    # images = [img.name for img in path.iterdir() if img.suffix in [".jpeg", ".png", ".jpg"]] # TODO Add more img types

    print(request.path)

    if request.htmx:
        return render(request, "galleries_partial.html", {"images": images})
    return render(request, "galleries.html", {"images": images})
