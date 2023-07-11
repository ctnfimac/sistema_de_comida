from django.contrib import admin
from web.models.administrador import Administrador

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    pass

