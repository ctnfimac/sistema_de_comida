from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from web.models.usuario import Usuario
from web.models.tipo import Tipo

class UsuarioModelTest(TestCase):

    def setUp(self):
        # Creo los 3 tipos de usuario que necesito para testear al usuario
        self.tipo1 = Tipo.objects.create(titulo='Cliente')
        self.tipo2 = Tipo.objects.create(titulo='Delivery')
        self.tipo3 = Tipo.objects.create(titulo='Comercio')

    def test_registro_usuario(self):
        url = reverse('web:registroView')
        datos = {
            'email': 'test@christianperalta.com', 
            'contrasenia': 'micontrasenia',
            'password2': 'micontrasenia',
            'telefono': '1144445555', 
            'tipo': '2'
        }
        response = self.client.post(url, datos)

        # verifico que redireccione a la pagina que quiero
        self.assertRedirects(response, reverse('web:home'))

        # Verificar que se creo un usuario nuevo
        self.assertEqual(Usuario.objects.count(), 1)

        # Verificar que los datos ingresados se guardaron correctamente
       
        usuarios_creados = Usuario.objects.filter(
            email= 'test@christianperalta.com'
        )
        usuario_obtenido = usuarios_creados.first()

        self.assertEqual(usuario_obtenido.tipo.titulo, 'Delivery')
        self.assertEqual(usuario_obtenido.email, 'test@christianperalta.com')
        self.assertEqual(usuario_obtenido.telefono, '1144445555')
        self.assertTrue(check_password('micontrasenia',usuario_obtenido.contrasenia))
       
    
    def test_registro_usuario_unico(self):
        pass