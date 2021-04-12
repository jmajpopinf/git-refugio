from django.conf.urls import url
from django.urls import path, include

from apps.usuario.views import RegistrarUsuario


urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name='registrar'),
]