#django
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

#python
import json

#django rest framwework
from rest_framework.test import APIClient
from rest_framework import status

#modelos
from web.models.usuario import Usuario
from web.models.tipo import Tipo


class UsuarioApiTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

        # agrego los 3 tipos de clientes
        cls.tipo1 = Tipo.objects.create(titulo='Cliente')
        cls.tipo2 = Tipo.objects.create(titulo='Delivery')
        cls.tipo3 = Tipo.objects.create(titulo='Comercio')

        # agrego dos usuarios
        cls.usuario = Usuario(
            nombre= "Christian2",
            apellido= "Peralta2",
            email= "testapi2@gmail.com",
            contrasenia= "123456",
            telefono= "46446645",
            habilitado= False,
            cuenta_activada= True,
            key_activacion= "eyJrZXlfYWN0aXZhY2lvbiI6ImNocmlzdGlhbmlwYy4xOTg3QGdtYWlsLmNvbSJ9:_V4bGoLbyErqqVZAMEUm1lt3zgwAOc01QdETPY1PZgc",
            tipo= cls.tipo1
        )

        cls.usuario2 = Usuario(
            nombre= "Christian3",
            apellido= "Peralta3",
            email= "testapi3@gmail.com",
            contrasenia= "abc",
            telefono= "46446666",
            habilitado= False,
            cuenta_activada= True,
            key_activacion= "wyJrZXlfYWN0aXZhY2lvbiI6ImNocmlzdGlhbmlwYy4xOTg3QGdtYWlsLmNvbSJ9:_V4bGoLbyErqqVZAMEUm1lt3zgwAOc01QdETPY1PZgc",
            tipo= cls.tipo2
        )

        cls.usuario.save()
        cls.usuario2.save()



    def test_obtengo_usuarios(self):
        url = reverse('api_usuario')
        response = self.client.get(url)
        result = json.loads(response.content)

        # verifico si la peticion se hace correctamente
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # verifico si la cantidad de usuarios obtenidos es uno
        self.assertEqual(len(result), 2)

        # verifico los campos obtenidos
        self.assertIn('id', result[0])
        self.assertIn('nombre', result[0])
        self.assertIn('apellido', result[0])
        self.assertIn('email', result[0])
        self.assertIn('contrasenia', result[0])
        self.assertIn('telefono', result[0])
        self.assertIn('habilitado', result[0])
        self.assertIn('cuenta_activada', result[0])
        self.assertIn('key_activacion', result[0])

        # verifico los valores de los campos si son correctos
        self.assertEqual(result[0]['id'], self.usuario.id)
        self.assertEqual(result[0]['nombre'], self.usuario.nombre)
        self.assertEqual(result[0]['apellido'], self.usuario.apellido)
        self.assertEqual(result[0]['contrasenia'], self.usuario.contrasenia)
        self.assertEqual(result[0]['telefono'], self.usuario.telefono)
        self.assertEqual(result[0]['habilitado'], self.usuario.habilitado)
        self.assertEqual(result[0]['cuenta_activada'], self.usuario.cuenta_activada)


    def test_obtengo_un_usuario(self):
        url = reverse('api_usuario_detail', kwargs={'pk':2})
        response = self.client.get(url)
        result = json.loads(response.content)

        # verifico si el codigo de la respuesta es correcto
        self.assertEqual(response.status_code, 200)

        # verifico que el json de la respuesta no este vacio
        self.assertNotEqual(len(result),0)
        
        # verifico que se encuentren los campos en la respuesta
        self.assertIn('id', result)
        self.assertIn('nombre', result)
        self.assertIn('apellido', result)
        self.assertIn('email', result)
        self.assertIn('contrasenia', result)
        self.assertIn('telefono', result)
        self.assertIn('habilitado', result)
        self.assertIn('cuenta_activada', result)
        self.assertIn('key_activacion', result)

        # verifico si el usuario retornado tiene los valores correctos
        self.assertEqual(result['id'], self.usuario2.id)
        self.assertEqual(result['nombre'], self.usuario2.nombre)
        self.assertEqual(result['apellido'], self.usuario2.apellido)
        self.assertEqual(result['email'], self.usuario2.email)
        self.assertEqual(result['contrasenia'], self.usuario2.contrasenia)
        self.assertEqual(result['telefono'], self.usuario2.telefono)
        self.assertEqual(result['habilitado'], self.usuario2.habilitado)
        self.assertEqual(result['cuenta_activada'], self.usuario2.cuenta_activada)
        self.assertEqual(result['key_activacion'], self.usuario2.key_activacion)




    def test_guardo_un_usuario(self):
        url = reverse('api_usuario')
        datos = {
            'nombre' : "Christian3",
            'apellido' : "Peralta3",
            'email': 'test4@christianperalta.com', 
            'contrasenia': 'micontrasenia4',
            'password2': 'micontrasenia4',
            'telefono': '11444455554', 
            'tipo': '2'
        }
        response = self.client.post(url, datos)

        # verifico si la respuesta es la de un usuario creado
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # verifico si hay 3 usuarios 
        self.assertEqual(Usuario.objects.count(),3)

        # verifico si los datos se guardaron correctamente
        usuario_creado = Usuario.objects.filter(email='test4@christianperalta.com').first()
        
        self.assertEqual(usuario_creado.nombre, 'Christian3')
        self.assertEqual(usuario_creado.apellido, 'Peralta3')
        self.assertEqual(usuario_creado.contrasenia, 'micontrasenia4')
        self.assertEqual(usuario_creado.telefono, '11444455554')
        self.assertEqual(usuario_creado.email, 'test4@christianperalta.com')
        self.assertEqual(usuario_creado.tipo.titulo, 'Delivery')
        self.assertEqual(usuario_creado.habilitado, False)

      

    def test_modifico_un_usuario(self):
        url = reverse('api_usuario_detail', kwargs={'pk':1})
        datos_nuevos = {
            "nombre": "Christian Modificado",
            "apellido": "Peralta Modificado",
            "email": "testapi@gmail.com",
            "contrasenia": "12345688",
            "telefono": "46446645",
        }

        response = self.client.put(url, 
                                   json.dumps(datos_nuevos), 
                                   headers={'content-type': 'application/json'}
                                   )
        
        # verifico que la respuesta sea correcta
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # verifico que efectivamente se cambiaron los valores de  nombre, apellido, email, contraseña, telefono
        usuario_modificado = Usuario.objects.get(pk=1)
        self.assertEqual(usuario_modificado.nombre, datos_nuevos['nombre'])
        self.assertEqual(usuario_modificado.apellido, datos_nuevos['apellido'])
        self.assertEqual(usuario_modificado.email, datos_nuevos['email'])
        self.assertEqual(usuario_modificado.contrasenia, datos_nuevos['contrasenia'])
        self.assertEqual(usuario_modificado.telefono, datos_nuevos['telefono'])



    def test_elimino_usuario(self):
        url = reverse('api_usuario_detail', kwargs={'pk':1})

        # verifico que hayan dos usuarios
        self.assertEqual(Usuario.objects.count(), 2)

        response = self.client.delete(url)

        # verifico si se ejecuto la operación
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # verifico que haya quedado un usuario
        self.assertEqual(Usuario.objects.count(), 1)

        # verifico que no haya usuario con el id = 1
        self.assertEqual(Usuario.objects.filter(pk=1).count(), 0)
        