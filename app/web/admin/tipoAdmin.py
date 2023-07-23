from django.contrib import admin
from web.models.tipo import Tipo

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    pass

