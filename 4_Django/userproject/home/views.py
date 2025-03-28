from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request): 
    if request.method == "POST":  
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password")  

    return render(request, 'login.html') 

def logoutUser(request):
    logout(request)
    return redirect("/login")
