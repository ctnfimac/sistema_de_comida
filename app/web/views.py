from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect

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


def administracion(request):
    context = {
        'title': 'Administrador'
    }
    return render(request, 'admin/administrador.html', context)


def comercioAdmin(request):
    context = {
        'title': 'Comercio Admin'
    }
    return render(request, 'admin/comercios.html', context)


def repartidorAdmin(request):
    context = {
        'title': 'Repartidor Admin'
    }
    return render(request, 'admin/repartidor.html', context)


def clienteAdmin(request):
    context = {
        'title': 'Cliente Admin'
    }
    return render(request, 'admin/cliente.html', context)

########################
#
# Usuarios: Registro
#
########################

# con view
class RegistroView(View):
    form_class = RegistroForm
    template_name = reverse_lazy('web:home')

    def post(self, request):
        form = self.form_class(request.POST)
        context = {
                'loginForm': LoginForm(),
                'contactoForm': ContactoForm(),
                'registroForm': form
            }
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.template_name)
        
        return render(request, self.template_name, context)