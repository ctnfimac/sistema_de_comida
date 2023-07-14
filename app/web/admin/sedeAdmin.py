from django.contrib import admin
from web.models.sede import Sede

@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    pass