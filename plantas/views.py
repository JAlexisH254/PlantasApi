from django.shortcuts import render
from rest_framework import generics
from plantas.serializers import AfeccionSerializer,CultivoSerializer,UsuarioSerializer
from plantas.models import Afeccion,Cultivo,Usuario
# Create your views here.

class AfeccionList(generics.ListAPIView):
    serializer_class = AfeccionSerializer
    queryset = Afeccion.objects.all()

class CultivoList(generics.ListAPIView):
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()

class UsuarioList(generics.ListAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    