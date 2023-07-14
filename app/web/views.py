from django.shortcuts import render
# from .forms import LoginForm
from web.forms.loginForm import LoginForm
from web.forms.contactoForm import ContactoForm


def home(request):
    loginForm = LoginForm()
    contactoForm = ContactoForm()
    context = {
        'loginForm': loginForm,
        'contactoForm': contactoForm
    }
    return render(request,'web/home.html', context)