from rest_framework.response import Response
from rest_framework.views import APIView
from web.api.serializers import UsuarioSerializer
from web.models.usuario import Usuario

class UsuarioApiView(APIView):
    
    def get(self, request):
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many = True)
        return Response(usuarios_serializer.data)