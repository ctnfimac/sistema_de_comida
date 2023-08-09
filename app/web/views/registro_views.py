from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import JsonResponse
from django.core.signing import Signer

from django.utils import timezone
from web.forms.registroForm import RegistroForm

from django.core.mail import send_mail
from web.models.usuario import Usuario


def registroRealizado(request, email):
    context = {
        'email': email
    }
    return render(request,'web/registro_realizado.html', context)



class RegistroView(FormView):
    form_class = RegistroForm
    template_name = reverse_lazy('web:home')
    success_url = reverse_lazy('web:home')

    def form_valid(self, form):
        registro_nuevo = form.save()

        url_activacion = 'http://127.0.0.1:8000/web/activarCuenta/{clave_activacion}'.format(clave_activacion=registro_nuevo.key_activacion)
        msj = f"Gracias por registrarse, para activar su cuenta ingrese al siguiente link {url_activacion}"
        send_mail(
            "Activación de la cuenta",
            msj,
            settings.ADMIN_USER_EMAIL,
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        return JsonResponse({'success': True, 'email': form.cleaned_data['email']})

    def form_invalid(self, form) -> JsonResponse:
        errors = form.errors
        return JsonResponse({'errors': errors}, status=400)
    


def activarCuenta(request, key):
    signer = Signer()
    context = {}
    dato = signer.unsign_object(key)
    # busco al usuario  con el email
    usuario = Usuario.objects.get(email=dato['key_activacion'])

    # verifico que las key sean iguales
    # si es así el campo habilitado lo pongo en true
    # y me redirige a una pantalla donde se hace el ingreso de datos
    # dependiento el tipo de usuario
    if usuario.key_activacion == key and usuario.cuenta_activada == False:
        print('son iguales')
        usuario.cuenta_activada = True
        usuario.fecha_activacion = timezone.now()
        usuario.save()
        
        #TODO: crear variable de sesión
        # para habilitar la cuenta tengo que completar los datos
        # dependiendo el perfil del usuario
        if usuario.tipo.titulo == 'Cliente':
            context = {'tipo':'cliente'}
            return render(request, 'admin/habilitar_cuenta.html',context)
    else:
        #TODO: hacer pagina 404
        print('Redirijo a una pantalla de Error')

    return JsonResponse({'respuesta': 'ok'})