from django.contrib import admin
from web.models.pedidomenu import PedidoMenu

@admin.register(PedidoMenu)
class PedidoMenuAdmin(admin.ModelAdmin):
    pass
