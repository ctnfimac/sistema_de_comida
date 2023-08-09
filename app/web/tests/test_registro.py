from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from web.models.usuario import Usuario
from web.models.tipo import Tipo
import json

class UsuarioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Creo los 3 tipos de usuario que necesito para testear al usuario
        cls.tipo1 = Tipo.objects.create(titulo='Cliente')
        cls.tipo2 = Tipo.objects.create(titulo='Delivery')
        cls.tipo3 = Tipo.objects.create(titulo='Comercio')

        cls.url_registroUsuario = reverse('web:registroView')

        # creo un usuario para la prueba de registro incorrecto
        cls.usuario_nuevo = Usuario(email = 'info@gmail.com',
                                    contrasenia = '123',
                                    telefono = '44446666',
                                    tipo = cls.tipo1)
        cls.usuario_nuevo.save()



    def test_registro_usuario_valido(self):
        url = reverse('web:registroView')

        # hago una solicitud post con datos correctos
        datos = {
            'email': 'test@christianperalta.com', 
            'contrasenia': 'micontrasenia',
            'password2': 'micontrasenia',
            'telefono': '1144445555', 
            'tipo': '2'
        }
        response = self.client.post(url, datos)
        response_data = json.loads(response.content)

        # verifico el código de estado
        self.assertEqual(response.status_code, 200)

        # Verificar que se creo un usuario nuevo
        self.assertEqual(Usuario.objects.count(), 2)

        # verifico que la respuesta es la esperada
        self.assertEqual(response_data['success'], True)
        self.assertEqual(response_data['email'], 'test@christianperalta.com')
        self.assertIsInstance(response, JsonResponse)


        # Verificar que los datos ingresados se guardaron correctamente
        usuarios_creados = Usuario.objects.filter(
            email= 'test@christianperalta.com'
        )
        usuario_obtenido = usuarios_creados.first()

        self.assertEqual(usuario_obtenido.tipo.titulo, 'Delivery')
        self.assertEqual(usuario_obtenido.email, 'test@christianperalta.com')
        self.assertEqual(usuario_obtenido.telefono, '1144445555')
        self.assertTrue(check_password('micontrasenia',usuario_obtenido.contrasenia))
       

    
    def test_registro_usuario_no_valido(self):
        """
        Pruebo que no se guarde registro cuando las contraseñas no son iguales,
        también cuando el email ingresado es uno ya existente
        """
        url = reverse('web:registroView')

        # hago una solicitud post con contraseñas distintas
        datos = {
            'email': 'test@christianperalta.com', 
            'contrasenia': 'micontraseniaMal',
            'password2': 'micontrasenia',
            'telefono': '1144445555', 
            'tipo': '2'
        }
        response = self.client.post(url, datos)

        # verifico el código de estado
        self.assertEqual(response.status_code, 400)

        # hago una solicitud post con email repetido
        datos = {
            'email': 'info@gmail.com', 
            'contrasenia': 'micontrasenia',
            'password2': 'micontrasenia',
            'telefono': '1144445555', 
            'tipo': '2'
        }
        response = self.client.post(url, datos)

        # verifico el código de estado
        self.assertEqual(response.status_code, 400)

        # verifico que siga habiendo un solo usuario cargado
        self.assertEqual(Usuario.objects.count(),1)

