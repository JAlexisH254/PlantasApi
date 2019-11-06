from rest_framework import serializers

from plantas.models import Enfermedad, Cultivo

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ["id", "nombre_enfermedad"]

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = ["id", "nombre_cultivo"]
    