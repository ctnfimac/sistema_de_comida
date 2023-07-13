from django.contrib import admin
from web.models.ganancia import Ganancia

@admin.register(Ganancia)
class GananciaAdmin(admin.ModelAdmin):
    pass
