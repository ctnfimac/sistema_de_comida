from django.db import models
from .usuario import Usuario


class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.RESTRICT)
    admin = models.CharField(max_length=30, null=False)

    class Meta:
        app_label = 'web'
        verbose_name_plural = 'Administradores'

    def __str__(self) -> str:
        return f'{self.admin}.{self.usuario}'
    