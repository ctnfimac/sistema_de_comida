from django.contrib import admin
from web.models.comercio import Comercio

@admin.register(Comercio)
class ComercioAdmin(admin.ModelAdmin):
    pass
