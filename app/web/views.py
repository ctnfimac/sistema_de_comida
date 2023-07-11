from django.shortcuts import render
from .forms import LoginForm

def home(request):
    loginForm = LoginForm()
    return render(request,'web/home.html', {'loginForm': loginForm})