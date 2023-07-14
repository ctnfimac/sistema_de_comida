from django.db import models
from .usuario import Usuario
from .pedido import Pedido


class Liquidacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    pedido = models.OneToOneField(Pedido, on_delete=models.RESTRICT)
    periodo_pago = models.DateField()
    remuneracion = models.DecimalField(max_digits=9, decimal_places=2)
    descuento = models.DecimalField(max_digits=7, decimal_places=2)
    neto = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        app_label = 'web'
