from django.db import models
from .cliente import Cliente
from .repartidor import Repartidor
from .comercio import Comercio


class Pedido(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete=models.RESTRICT)
    repartidor = models.ForeignKey(Repartidor, null=True, on_delete=models.SET_NULL)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    hora_alta = models.DateTimeField()
    penalizado = models.DecimalField(max_digits=7 ,decimal_places=2, default=0)
    estado = models.PositiveSmallIntegerField(default=1)
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=0)

    class Meta:
        app_label = 'web'  
        verbose_name_plural = 'Pedidos'  
    
    def __str__(self) -> str:
        return f'Pedido realizado por: {self.cliente}'