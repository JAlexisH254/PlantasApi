from rest_framework import serializers

from plantas.models import Enfermedad

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ["id", "nombre_enfermedad"]
    