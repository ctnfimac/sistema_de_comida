from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path("", views.home, name="home"),
    path("administracion", views.administracion, name="administracion"),
    path("comercioadmin", views.comercioAdmin, name="comercioAdmin"),
    path("repartidoradmin", views.repartidorAdmin, name="repartidorAdmin"),
    path("clienteadmin", views.clienteAdmin, name="clienteAdmin"),
]