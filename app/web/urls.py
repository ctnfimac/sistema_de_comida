from django.urls import path
from web.views.public_views import home
from web.views.registro_views import (
    RegistroView, 
    activarCuenta,
    registroRealizado
)

from web.views.administracion_views import (
    administracion,
    comercioAdmin,
    repartidorAdmin,
    clienteAdmin
)

app_name = 'web'

urlpatterns = [
    # public
    path("", home, name="home"),

    # Administración
    path("administracion", administracion, name="administracion"),
    path("comercioadmin", comercioAdmin, name="comercioAdmin"),
    path("repartidoradmin", repartidorAdmin, name="repartidorAdmin"),
    path("clienteadmin", clienteAdmin, name="clienteAdmin"),

    # Registro de usuarios
    path("registroRealizado/<str:email>", registroRealizado, name="registroRealizado"),
    path("activarCuenta/<str:key>", activarCuenta, name="activarCuenta"),
    path("registroView", RegistroView.as_view(), name='registroView')
]