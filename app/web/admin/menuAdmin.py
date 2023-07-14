from django.contrib import admin
from web.models.menu import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass
