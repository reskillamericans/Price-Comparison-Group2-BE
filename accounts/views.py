from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from django import forms
from .forms import LoginForm, RegisterForm

User = get_user_model()



def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
         form = RegisterForm(request.POST)
         if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
             messages.success(request, 'Account was created for ' + user)
             
             return redirect('login')
             #return HttpResponseRedirect('login')
            
        
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            # user is valid and active
            login(request, user)
            return redirect("/")
        else:
        
            request.session['invalid_user'] == True
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")
