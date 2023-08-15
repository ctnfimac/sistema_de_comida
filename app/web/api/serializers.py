from rest_framework import serializers
from web.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    
    # def create(self, validated_data):
    #     return Usuario.objects.create(**validated_data)