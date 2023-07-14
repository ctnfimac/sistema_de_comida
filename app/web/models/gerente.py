from django.db import models
from .usuario import Usuario
from .comercio import Comercio


class Gerente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.RESTRICT)
    comercio = models.ForeignKey(Comercio, on_delete=models.RESTRICT)
    cuil = models.CharField(max_length=11, null=False)

    class Meta:
        app_label = 'web'

    def __str__(self) -> str:
        return f'{self.usuario}'