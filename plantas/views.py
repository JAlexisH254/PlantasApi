from django.shortcuts import render
from rest_framework import generics
from plantas.serializers import EnfermedadSerializer
from plantas.models import Enfermedad
# Create your views here.

class EnfermedadList(generics.GenericAPIView):
    serializer_class = EnfermedadSerializer
    queryset = Enfermedad.objects.all()