from django.urls import path
from . import views
from .views import RegistroView

app_name = 'web'

urlpatterns = [
    path("", views.home, name="home"),
    path("administracion", views.administracion, name="administracion"),
    path("comercioadmin", views.comercioAdmin, name="comercioAdmin"),
    path("repartidoradmin", views.repartidorAdmin, name="repartidorAdmin"),
    path("clienteadmin", views.clienteAdmin, name="clienteAdmin"),

    path("registroView", RegistroView.as_view(), name='registroView')
]