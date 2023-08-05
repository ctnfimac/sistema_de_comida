from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path("", views.home, name="home"),
    path("administracion", views.administracion, name="administracion"),
    path("comercioadmin", views.comercioAdmin, name="comercioAdmin"),
    path("repartidoradmin", views.repartidorAdmin, name="repartidorAdmin"),
    path("clienteadmin", views.clienteAdmin, name="clienteAdmin"),
    path("registroRealizado/<str:email>", views.registroRealizado, name="registroRealizado"),
    path("activarCuenta/<str:key>", views.activarCuenta, name="activarCuenta"),

    path("registroView", views.RegistroView.as_view(), name='registroView')
]