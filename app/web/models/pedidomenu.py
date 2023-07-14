from django.db import models
from .pedido import Pedido
from .menu import Menu


class PedidoMenu(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    menu = models.ForeignKey(Menu, on_delete=models.RESTRICT)
    cantidad = models.PositiveSmallIntegerField(default=1)

    class Meta:
        app_label = 'web'  
        verbose_name_plural = 'Menus del Pedido'  
        unique_together = (('pedido', 'menu'),)
        
    
    def __str__(self) -> str:
        return f'{self.cantidad} {self.producto} del comercio {self.comercio}'