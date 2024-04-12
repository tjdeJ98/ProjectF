from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_staff == True:
            auth.login(request,user)
            messages.success(request, 'You are Logged in')
            return redirect('gallerie')
        
        else:
            messages.error(request,'Your Username or Password is incorrect')
            return redirect('login')
        return
    else:
        if request.htmx:
            return render(request, "login_partial.html")
        return render(request, "login.html")


    


