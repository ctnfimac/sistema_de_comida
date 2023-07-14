from django.contrib import admin
from web.models.cliente import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass
