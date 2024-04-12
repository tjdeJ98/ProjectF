from django.shortcuts import render

# Create your views here.


def contact(request):
    if request.htmx:
        return render(request, "contact_partial.html")
    return render(request, "contact.html")
