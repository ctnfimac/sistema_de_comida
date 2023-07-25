from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models.usuario import Usuario
from .models.tipo import Tipo

# from .forms import LoginForm
from web.forms.loginForm import LoginForm
from web.forms.contactoForm import ContactoForm
from web.forms.registroForm import RegistroForm

from django.db import IntegrityError


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

# con método
def usuarioCrud(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email','')
            contrasenia = request.POST.get('password','')
            telefono = request.POST.get('telefono','')
            tipo = Tipo.objects.get(pk = int(request.POST.get('tipo','')))
            
            usuarioNuevo = Usuario(
                tipo= tipo, 
                email= email, 
                telefono= telefono, 
                contrasenia= contrasenia
            )
            usuarioNuevo.save()
        
        elif request.method == 'GET':
            print('Estoy en el GET')

        else:
            print('tipo de peticion desconocida')
        
    except IntegrityError:
        print('Problemas al querer dar de alta el usuario')
    finally:
        return redirect(reverse('web:home'))
    
    
# class UsuarioView(View):
    
#     def get(self, request):
#         print('ESTOY EN GET')

#     def post(self, request):
#         print('ESTOY EN POST')