from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import LostItem, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user() #already authenticated, if return none it will execute the next else block
            login(request, user)
            return redirect("/home")
        
    else:
        form = AuthenticationForm()

    return render(request,"login.html", {"form":form})


def home(request):
    return render(request, 'home.html')

