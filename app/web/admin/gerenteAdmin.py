from django.contrib import admin
from web.models.gerente import Gerente

@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    pass