from django.db import models
from .usuario import Usuario
from .localidad import Localidad



class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.RESTRICT)
    localidad = models.ForeignKey(Localidad, on_delete=models.RESTRICT)
    calle = models.CharField(max_length=30, null=False)
    altura = models.CharField(max_length=30, null=False)
    direccion = models.EmailField(max_length=50, null=False, unique=True)

    class Meta:
        app_label = 'web'
    
    def __str__(self) -> str:
        return f'{self.usuario}'
    
