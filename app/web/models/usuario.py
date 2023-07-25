from django.db import models
from .tipo import Tipo

class Usuario(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True)
    contrasenia = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=30, null=False)
    habilitado = models.BooleanField(default=False)
    cuenta_activada = models.BooleanField(default=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_activacion = models.DateTimeField(null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.RESTRICT, default=0)


    class Meta:
        app_label = 'web'


    def __str__(self) -> str:
        return f'{self.nombre} {self.nombre}, email: {self.email}'
    