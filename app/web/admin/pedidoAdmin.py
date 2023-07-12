from django.contrib import admin
from web.models.pedido import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    pass
