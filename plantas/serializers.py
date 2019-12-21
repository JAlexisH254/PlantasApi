from rest_framework import serializers

from plantas.models import Afeccion, Cultivo, Usuario, CultivoAfeccion, UsuarioCultivo, Prevencion, Diagnostico, Tratamiento, TratamientoAfeccion 

#Búsqueda de Afección
class BusquedaAfeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afeccion
        fields = ["id", "nombre_afeccion", "causa_afeccion"]

class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = ["id", "nombre_cultivo","guia_cultivo","imagen_cultivo"]

#Muestra datos del usuario
class UsuarioDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [ "nombre_usuario", "contrasenia_usuario", "correo_usuario", "telefono_usuario" ]

#Login con usuario y contraseña / los otros logins se manejarán con Firebase

#Datos usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [ "id", "correo_usuario", "contrasenia_usuario", "nombre_usuario" , "telefono_usuario","imagen_usuario"]


class UsuarioLoginSerializer(serializers.ModelSerializer):
    Usuario = UsuarioSerializer(many=False)
    class Meta:
        model = Usuario
        fields = [ "Usuario"]

class CultivoAfeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultivoAfeccion
        fields = ["id", "nombre_usuario"]    

class DiagnosticoSerializer(serializers.ModelSerializer):
   afeccion = BusquedaAfeccionSerializer(many=False)
   class Meta:
        model = Diagnostico
        fields = ["id", "afeccion","fecha_diagnostico"]  


class DiagnosticoRegistroSerializer(serializers.ModelSerializer):
   class Meta:
        model = Diagnostico
        fields = ["id", "afeccion","fecha_diagnostico"]  


#tabla de Jesus
class UsuarioCultivoSerializer(serializers.ModelSerializer):
    Usuario = UsuarioSerializer(many=False)
    Diagnostico = DiagnosticoSerializer(many=False)
    Cultivo = CultivoSerializer(many=False)
    class Meta:
        model = UsuarioCultivo
        fields = ["id", "Usuario","Diagnostico","Cultivo","imagen_usuarioCultivo"]

class UsuarioCultivoRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCultivo
        fields = ["id", "Usuario","Cultivo","imagen_usuarioCultivo"]

class PrevencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prevencion
        fields = ["id", "nombre_usuario"]


class TratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamiento
        fields = ["id", "descripcion_tratamiento"]

class TratamientoAfeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoAfeccion
        fields = ["id", "nombre_usuario"]