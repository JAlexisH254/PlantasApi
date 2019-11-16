from rest_framework import serializers

from plantas.models import Afeccion, Cultivo, Usuario

class AfeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afeccion
        fields = ["id", "nombre_afeccion"]

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = ["id", "nombre_cultivo"]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "nombre_usuario"]    