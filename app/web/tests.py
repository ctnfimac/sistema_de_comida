from django.test import TestCase
from django.urls import reverse
from web.models.usuario import Usuario
from web.models.tipo import Tipo

class UsuarioModelTest(TestCase):

    def setUp(self):
        # Creo los 3 tipos de usuario que necesito para testear al usuario
        tipo1 = Tipo(titulo='Cliente')
        tipo1.save()
        tipo2 = Tipo(titulo='Delivery')
        tipo2.save()
        tipo3 = Tipo(titulo='Comercio')
        tipo3.save()


    # usuarioCrud
    def test_registro_usuario(self):
        url = reverse('web:usuarioCrud')
        datos = {
            'email': 'test@christianperalta.com', 
            'password': 'micontrasenia',
            'telefono': '1144445555', 
            'tipo': '2'
        }
        response = self.client.post(url, datos)

        # verifico que redireccione a la pagina que quiero
        self.assertRedirects(response, reverse('web:home'))
        
        # verifico que tenga el codigo de redirección correcto
        self.assertEqual(response.status_code, 302)

        tipo = Tipo.objects.get(pk=2)
        # verifico que el tipo a verificar sea el correcto
        self.assertEqual(tipo.titulo,'Delivery')

        usuarios_creados = Usuario.objects.filter(
            email= 'test@christianperalta.com', 
            contrasenia= 'micontrasenia',
            telefono= '1144445555', 
            tipo= tipo
        )

        # Verificar que se creo un usuario nuevo
        self.assertEqual(usuarios_creados.count(), 1)
   
        usuario_obtenido = usuarios_creados.first()

        # Verificar que los valores de los campos sean los correctos
        self.assertEqual(usuario_obtenido.tipo.titulo, 'Delivery')
        self.assertEqual(usuario_obtenido.email, 'test@christianperalta.com')
        self.assertEqual(usuario_obtenido.telefono, '1144445555')
        self.assertEqual(usuario_obtenido.contrasenia, 'micontrasenia')
