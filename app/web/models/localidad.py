from django.db import models


class Localidad(models.Model):
    descripcion = models.CharField(max_length=30, null=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        app_label = 'web'
        verbose_name_plural = 'Localidades'

    def __str__(self) -> str:
        return self.descripcion
    