from django.shortcuts import render
from rest_framework import generics
from plantas.serializers import EnfermedadSerializer,CultivoSerializer
from plantas.models import Enfermedad,Cultivo
# Create your views here.

class EnfermedadList(generics.ListAPIView):
    serializer_class = EnfermedadSerializer
    queryset = Enfermedad.objects.all()

class CultivoList(generics.ListAPIView):
    serializer_class = CultivoSerializer
    queryset = Cultivo.objects.all()