from django.conf.urls import url
from django.urls import path

from rest_framework.authtoken import views
from plantas.views import EnfermedadList

urlpatterns = [
    path('enfermedades/', EnfermedadList.as_view()),
    # url(r'^api-token-auth/', views.obtain_auth_token),
]