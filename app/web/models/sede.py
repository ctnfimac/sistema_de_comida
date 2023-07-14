from django.db import models
from .comercio import Comercio

class Sede(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete=models.RESTRICT)
    codigo = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False, unique=True)
    calle = models.CharField(max_length=30, null=False)
    altura = models.CharField(max_length=30, null=False)
    sede_activa = models.BooleanField(default=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        app_label = 'web'
        
    def __str__(self) -> str:
        return f'{self.codigo}'