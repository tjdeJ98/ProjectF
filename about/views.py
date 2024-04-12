from django.shortcuts import render

# Create your views here.


def about(request):
    if request.htmx:
        return render(request, "about_partial.html")
    return render(request, "about.html")
