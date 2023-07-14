from django.db import models
from .usuario import Usuario


class Repartidor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.RESTRICT)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=8, null=False)
    cuil = models.CharField(max_length=11, null=False)
    estado = models.SmallIntegerField(null=True, default=0)

    class Meta:
        app_label = 'web'  
        verbose_name_plural = 'Repartidores'  
    
    def __str__(self) -> str:
        return f'{self.usuario}'