from django.urls import path
from web.api.api import UsuarioApiView, UsuarioDetailView

urlpatterns = [
    path('usuario', UsuarioApiView.as_view(), name='api_usuario'),
    path('usuario/<int:pk>', UsuarioDetailView.as_view(), name='api_usuario_detail')
]