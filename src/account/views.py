from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLogForm, UserRegForm

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegForm()
    return render(request, 'acc/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLogForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = UserLogForm()
    return render(request, 'acc/login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('login')
