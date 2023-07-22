from django.shortcuts import render
# from .forms import LoginForm
from web.forms.loginForm import LoginForm
from web.forms.contactoForm import ContactoForm
from web.forms.registroForm import RegistroForm


def home(request):
    loginForm = LoginForm()
    contactoForm = ContactoForm()
    registroForm = RegistroForm()
    context = {
        'loginForm': loginForm,
        'contactoForm': contactoForm,
        'registroForm': registroForm
    }
    return render(request,'web/home.html', context)