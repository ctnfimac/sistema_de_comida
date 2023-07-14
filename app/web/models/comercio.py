from django.db import models
from .usuario import Usuario


class Comercio(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.RESTRICT)
    cuit = models.CharField(max_length=11, null=False)
    
    class Meta:
        app_label = 'web'
        
    def __str__(self) -> str:
        return f'{self.usuario}'
    