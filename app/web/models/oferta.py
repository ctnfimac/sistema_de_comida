from django.db import models
from .menu import Menu

class Oferta(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.RESTRICT)
    fecha = models.DateField(unique=True)
   
    class Meta:
        app_label = 'web'  

    
    def __str__(self) -> str:
        return f'{self.menu}, ofertada el día {self.fecha}'