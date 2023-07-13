from django.db import models
from .pedido import Pedido

class Entrega(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.RESTRICT)
    fecha_retiro = models.DateTimeField()
    fecha_entrega = models.DateTimeField()
   
    class Meta:
        app_label = 'web'  
        constraints = [
            models.UniqueConstraint(
                fields=['id','pedido'], name='unique_entrega_pedido'
            )
        ]

