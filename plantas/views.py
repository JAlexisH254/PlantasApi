from django.shortcuts import render
from rest_framework import generics
from plantas.serializers import *
from datetime import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import *
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

class UsuarioCultivoRegistrarList(generics.CreateAPIView):
    serializer_class = UsuarioCultivoRegistroSerializer

    def perform_create(self, serializer):
        uc = serializer.save()
        #Busco su afeccion
        a = Afeccion.objects.get(id=1)
        #fecha=datetime.today, hora=datetime.now
        d = Diagnostico(afeccion=a, fecha_diagnostico=datetime.today(), hora_diagnostico=datetime.now())
        # d = Diagnostico(afeccion=a)
        d.save()
        uc.Diagnostico = d
        uc.save()

class UsuarioRegistrarList(generics.CreateAPIView):
    serializer_class = UsuarioLoginSerializer

class UsuarioCultivoListTodos(generics.ListAPIView):
    serializer_class = UsuarioCultivoSerializer
    queryset = UsuarioCultivo.objects.all()

class UsuarioCultivoList(generics.ListAPIView):
    serializer_class = UsuarioCultivoSerializer
    queryset = UsuarioCultivo.objects.all()

    def get_queryset(self):
        usuarioid = self.kwargs['Usuario_id']
        u = Usuario.objects.get(id = usuarioid)
        return UsuarioCultivo.objects.filter(Usuario_id=u)

class PrevencionList(generics.ListAPIView):
    serializer_class = PrevencionSerializer
    queryset = Prevencion.objects.all()

class DiagnosticoList(generics.ListAPIView):
    serializer_class = DiagnosticoSerializer
    queryset = Diagnostico.objects.all()

class DiagnosticoRegistroList(generics.CreateAPIView):
    serializer_class = DiagnosticoSerializer
    queryset = Diagnostico.objects.all()

class TratamientoList(generics.ListAPIView):
    serializer_class = TratamientoSerializer
    queryset = Tratamiento.objects.all()

class TratamientoAfeccionList(generics.ListAPIView):
    serializer_class = TratamientoAfeccionSerializer
    queryset = TratamientoAfeccion.objects.all()

class RegistrarDiagnosticoCultivo(APIView):

     def post(self, request, format=None):
        print(request.data)
        usuario = request.data["usuario"]
        enfermedad = request.data["enfermedad"]
        afecciones = Afeccion.objects.all()
        for a in afecciones:
            if a.nombre_afeccion == enfermedad:
                enf = a

        cultivo = request.data["cultivo"]
        imagen = request.data['image']
        diagnostico = Diagnostico()
        diagnostico.afeccion = enf
        diagnostico.fecha_diagnostico = datetime.today()
        diagnostico.hora_diagnostico = datetime.now()
        diagnostico.save()


        u = UsuarioCultivo() #llenas los valores
        u.Usuario = Usuario.objects.get(pk=usuario)
        u.Cultivo = Cultivo.objects.get(pk=cultivo)
        u.Diagnostico = diagnostico
        u.imagen_usuarioCultivo = imagen
        u.save()
        return Response({"response" : "ok"})
