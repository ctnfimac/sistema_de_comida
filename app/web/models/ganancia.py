from django.db import models

class Ganancia(models.Model):
    fecha = models.DateField(unique=True)
    monto = models.DecimalField(max_digits=9, decimal_places=2)
   
    class Meta:
        app_label = 'web'  


