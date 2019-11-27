from django.conf.urls import url
from django.urls import path

from rest_framework.authtoken import views
from plantas.views import *

urlpatterns = [
    path('enfermedades/', AfeccionList.as_view()),
    path('cultivos/', CultivoList.as_view()),
    path('historialgeneral/', UsuarioCultivoList.as_view()),
    # url(r'^api-token-auth/', views.obtain_auth_token),
]