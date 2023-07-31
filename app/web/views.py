from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView
from django.http import HttpResponse, JsonResponse

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
        form.save()
        return JsonResponse({'success': True, 'email': form.cleaned_data['email']})

    def form_invalid(self, form) -> HttpResponse:
        #TODO: VAlidar error cuando hay contraseñas distintas
         # validar error si el usuario ya existe
         # validar error si el email no es valido
        #print('ERROR')
        #print(form)
        #return super().form_invalid(form)
        # return HttpResponse("form is invalid.. this is just an HttpResponse object")
        # context = {
        #     'loginForm': LoginForm(),
        #     'contactoForm': ContactoForm,
        #     'registroForm': form
        # }
        # return render('web/home.html', context)
        #return HttpResponseRedirect(reverse_lazy('web:home', kwargs={'registroForm':form.__dict__}))
        errors = form.errors.as_json()
        #print(errors)
        return JsonResponse({'errors': errors}, status=400)
        #return JsonResponse({'status': False}, status=500)
    