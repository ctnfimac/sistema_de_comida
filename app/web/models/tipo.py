from django.db import models


class Tipo(models.Model):
    titulo = models.CharField(max_length=20, null=False, unique=True)

    class Meta:
        app_label = 'web'

    def __str__(self) -> str:
        return f'{self.titulo}'
    