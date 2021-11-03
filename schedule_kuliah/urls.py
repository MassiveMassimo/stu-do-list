from django.urls import path
from .views import index, add_matkul, add_jadwal, delete_jadwal, get_jadwal

app_name = "schedule"

urlpatterns = [
    path('', index, name='index'),
    path('get-jadwal/<str:user_id>', get_jadwal, name='get_jadwal'),
    path('add-matkul/', add_matkul, name='add_matkul'),
    path('add-jadwal/<str:matkul_id>', add_jadwal, name='add_jadwal'),
    path('delete-jadwal/<str:jadwal_id>', delete_jadwal, name="delete_jadwal"),
]