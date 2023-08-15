from django.urls import path
from web.api.api import UsuarioApiView

urlpatterns = [
    path('usuario', UsuarioApiView.as_view(), name='api_usuario')
]