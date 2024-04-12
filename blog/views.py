from django.shortcuts import render
from blog.models import BlogPost


def blog_view(request):
    blogposts = BlogPost.objects.all()

    if request.htmx:
        return render(request, "blog_partial.html", {"blogpost": blogposts})
    return render(request, "blog.html", {"blogpost": blogposts})


