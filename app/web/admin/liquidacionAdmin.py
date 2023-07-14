from django.contrib import admin
from web.models.liquidacion import Liquidacion

@admin.register(Liquidacion)
class LiquidacionAdmin(admin.ModelAdmin):
    pass
