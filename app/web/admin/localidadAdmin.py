from django.contrib import admin
from web.models.localidad import Localidad

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    pass
