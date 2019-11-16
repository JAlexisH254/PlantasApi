from rest_framework import serializers

from plantas.models import Afeccion, Cultivo, Usuario, CultivoAfeccion, UsuarioCultivo, Prevencion, Diagnostico, Tratamiento, TratamientoAfeccion 

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

class CultivoAfeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultivoAfeccion
        fields = ["id", "nombre_usuario"]    

class UsuarioCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCultivo
        fields = ["id", "nombre_usuario"]    

class PrevencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prevencion
        fields = ["id", "nombre_usuario"]    

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ["id", "nombre_usuario"]                                    

class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ["id", "nombre_usuario"]                                    

class TratamientoAfeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoAfeccion
        fields = ["id", "nombre_usuario"]                                                    