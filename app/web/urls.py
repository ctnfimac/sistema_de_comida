from django.urls import path
from . import views
# from .views import UsuarioView

app_name = 'web'

urlpatterns = [
    path("", views.home, name="home"),
    path("administracion", views.administracion, name="administracion"),
    path("comercioadmin", views.comercioAdmin, name="comercioAdmin"),
    path("repartidoradmin", views.repartidorAdmin, name="repartidorAdmin"),
    path("clienteadmin", views.clienteAdmin, name="clienteAdmin"),
    
    path("usuarioCrud", views.usuarioCrud, name="usuarioCrud"),
    # path("usuarioRegistro/", UsuarioView.as_view())
]