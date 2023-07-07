from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False, unique=True)
    contrasenia = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=30, null=False)
    habilitado = models.BooleanField(default=False)
    cuenta_activada = models.BooleanField(default=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_activacion = models.DateTimeField(null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.nombre} {self.nombre}, email: {self.email}'
    


class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.RESTRICT)
    admin = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return f'{self.admin}.{self.usuario}'
    


class Localidad(models.Model):
    descripcion = models.CharField(max_length=30, null=False)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.descripcion
    

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.RESTRICT)
    localidad = models.ForeignKey(Localidad, on_delete=models.RESTRICT)
    calle = models.CharField(max_length=30, null=False)
    altura = models.CharField(max_length=30, null=False)
    direccion = models.EmailField(max_length=50, null=False, unique=True)
    
    def __str__(self) -> str:
        return f'{self.usuario}'