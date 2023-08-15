from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from web.api.serializers import UsuarioSerializer
from web.models.usuario import Usuario


class UsuarioApiView(APIView):

    def get(self, request):
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many = True)
        return Response(usuarios_serializer.data)
    
    def post(self, request, format=None):
        usuario_serializer = UsuarioSerializer(data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioDetailView(APIView):

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format = None):
        usuario = self.get_object(pk)
        usuario_serializer = UsuarioSerializer(usuario)
        return Response(usuario_serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario_serializer = UsuarioSerializer(usuario, request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
