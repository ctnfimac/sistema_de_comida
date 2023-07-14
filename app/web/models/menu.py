from django.db import models
from .comercio import Comercio
from .producto import Producto


class Menu(models.Model):
    comercio = models.ForeignKey(Comercio, on_delete=models.RESTRICT)
    producto = models.ManyToManyField(Producto, related_name='menu_producto')
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='uploads')
    precio = models.DecimalField(max_digits=7 ,decimal_places=2)
    disponible = models.BooleanField(default=True)
    en_stock = models.BooleanField(default=True) 
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        app_label = 'web'  
        verbose_name_plural = 'Menus'  
    
    def __str__(self) -> str:
        return f'{self.usuario}'