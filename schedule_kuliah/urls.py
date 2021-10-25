from django.urls import path
from .views import index, add_matkul, add_jadwal

module_name = "schedule"

urlpatterns = [
    path('', index, name='index'),
    path('add_matkul/', add_matkul, name='add_matkul'),
    path('add_jadwal/<str:matkul_id>', add_jadwal, name='add_jadwal'),
]