from django.contrib import admin
from web.models.producto import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass
