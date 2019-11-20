from django.shortcuts import render
from rest_framework import generics
from plantas.serializers import *
#AfeccionSerializer,CultivoSerializer,UsuarioSerializer, CultivoAfeccionSerializer, UsuarioCultivoSerializer, PrevencionSerializer, DiagnosticoSerializer, TratamientoSerializer, TratamientoAfeccionSerializer 
from plantas.models import *
#Afeccion, Cultivo, Usuario, CultivoAfeccion, UsuarioCultivo, Prevencion, Diagnostico, Tratamiento, TratamientoAfeccion 

# Create your views here.

class AfeccionList(generics.ListAPIView):
    serializer_class = BusquedaAfeccionSerializer
    queryset = Afeccion.objects.all()

class CultivoList(generics.ListAPIView):
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()

class UsuarioList(generics.ListAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class CultivoAfeccionList(generics.ListAPIView):
    serializer_class = CultivoAfeccionSerializer
    queryset = CultivoAfeccion.objects.all()

class UsuarioCultivoList(generics.ListAPIView):
    serializer_class = UsuarioCultivoSerializer
    queryset = UsuarioCultivo.objects.all()        

class PrevencionList(generics.ListAPIView):
    serializer_class = PrevencionSerializer
    queryset = Prevencion.objects.all()

class DiagnosticoList(generics.ListAPIView):
    serializer_class = DiagnosticoSerializer
    queryset = Diagnostico.objects.all()

class TratamientoList(generics.ListAPIView):
    serializer_class = TratamientoSerializer
    queryset = Tratamiento.objects.all()

class TratamientoAfeccionList(generics.ListAPIView):
    serializer_class = TratamientoAfeccionSerializer
    queryset = TratamientoAfeccion.objects.all()

