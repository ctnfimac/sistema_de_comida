from django.contrib import admin
from web.models.entrega import Entrega

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    pass
