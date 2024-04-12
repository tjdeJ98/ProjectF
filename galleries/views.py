from django.shortcuts import render
from os import listdir
from pathlib import Path
from django.conf import settings
# Create your views here.


def galleries(request):
    # path = Path(r"")
    # images = [img for img in path.iterdir()]
    # images = listdir(r"theme\static\media\gallerie")
    path = Path(r"theme\static\media\gallerie")
    images = [img.name for img in path.iterdir() if img.suffix in [".jpeg", ".png", ".jpg"]]
    
    if request.htmx:
        return render(request, "galleries_partial.html", {"images": images})
    return render(request, "galleries.html", {"images": images})
