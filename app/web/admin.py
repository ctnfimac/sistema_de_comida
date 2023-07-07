from django.contrib import admin
from .models import Usuario, Administrador, Localidad, Cliente

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    pass


@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass
