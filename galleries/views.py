from django.shortcuts import render

# Create your views here.


def galleries(request):
    return render(request, "about.html")
