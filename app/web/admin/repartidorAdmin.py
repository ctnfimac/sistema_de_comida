from django.contrib import admin
from web.models.repartidor import Repartidor


@admin.register(Repartidor)
class RepartidorAdmin(admin.ModelAdmin):
    pass
