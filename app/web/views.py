from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView
from django.http import HttpResponse, JsonResponse

from web.forms.loginForm import LoginForm
from web.forms.contactoForm import ContactoForm
from web.forms.registroForm import RegistroForm

from django.core.mail import send_mail


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


def registroRealizado(request, email):
    context = {
        'email': email
    }
    return render(request,'web/registro_realizado.html', context)


########################
#
# Usuarios: Registro
#
########################

class RegistroView(FormView):
    form_class = RegistroForm
    template_name = reverse_lazy('web:home')
    success_url = reverse_lazy('web:home')

    def form_valid(self, form):
        registro_nuevo = form.save()

        url_activacion = 'http://127.0.0.1:8000/web/activarCuenta/{clave_activacion}/'.format(clave_activacion=registro_nuevo.key_activacion)
        msj = f"Gracias por registrarse, para activar su cuenta ingrese al siguiente link {url_activacion}"
        send_mail(
            "Activación de la cuenta",
            msj,
            settings.ADMIN_USER_EMAIL,
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        return JsonResponse({'success': True, 'email': form.cleaned_data['email']})

    def form_invalid(self, form) -> HttpResponse:
        errors = form.errors
        return JsonResponse({'errors': errors}, status=400)