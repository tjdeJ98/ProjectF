from django.shortcuts import render
from os import listdir
from pathlib import Path
from django.conf import settings
# Create your views here.


def galleries(request):
    # path = Path(r"")
    # images = [img for img in path.iterdir()]
    # images = listdir(r"theme\static\media\gallerie")
    return render(request, "galleries.html")
