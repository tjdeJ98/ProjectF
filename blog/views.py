from django.shortcuts import render
from django.http import HttpResponse


def blog_view(request):
    if request.htmx:
        return render(request, "blog_partial.html")
    return render(request, "blog.html")


