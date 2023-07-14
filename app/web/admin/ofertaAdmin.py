from django.contrib import admin
from web.models.oferta import Oferta

@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    pass
