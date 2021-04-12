from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index_mascota, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete, listado

urlpatterns = [
    path('', index_mascota, name='index_mascota'),
    path('nuevo/', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    path('listar/', login_required(MascotaList.as_view()), name='mascota_listar'),
    path('editar/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
    path('eliminar/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
    path('listado/', listado, name='listado')#para acceder e objetos serializados
]