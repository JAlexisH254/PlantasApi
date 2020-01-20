from django.conf.urls import url
from django.urls import path

from rest_framework.authtoken import views
from plantas.views import *

urlpatterns = [
    path('enfermedades/', AfeccionList.as_view()),
    path('cultivos/', CultivoList.as_view()),
    path('historialgeneral/', UsuarioCultivoListTodos.as_view()),
    path('historial/<int:Usuario_id>', UsuarioCultivoList.as_view()),
    path('historialregistro/', UsuarioCultivoRegistrarList.as_view()),
    path('usuarioregistro/', UsuarioRegistrarList.as_view()),
    path('diagnosticolista/', DiagnosticoList.as_view()),
    path('RegistrarDiagnosticoCultivo/', RegistrarDiagnosticoCultivo.as_view()),

    # url(r'^api-token-auth/', views.obtain_auth_token),
]