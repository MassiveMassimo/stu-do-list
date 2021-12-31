from django.urls import path
from .views import *
app_name = "schedule"

urlpatterns = [
    path('', index, name='index'),
    path('get-jadwal/<str:user_id>', get_jadwal, name='get_jadwal'),
    path('add-matkul/', add_matkul, name='add_matkul'),
    path('add-jadwal/<str:matkul_id>', add_jadwal, name='add_jadwal'),
    path('delete-jadwal/<str:jadwal_id>', delete_jadwal, name="delete_jadwal"),
    path('delete-matkul/<str:matkul_id>', delete_matkul, name="delete_matkul"),
    
    # API
    path('api/get-jadwal/<str:user_id>', api_get_jadwal, name='api_get_jadwal'),
    path('api/get-matkul/<str:user_id>', api_get_matkul, name='api_get_matkul'),
    path('api/add-matkul/<str:user_id>', api_add_matkul, name='api_add_matkul'),
    path('api/add-jadwal/<str:matkul_id>', api_add_jadwal, name='api_add_jadwal'),
    path('api/delete-jadwal/<str:jadwal_id>', api_delete_jadwal, name="api_delete_jadwal"),
    path('api/delete-matkul/<str:matkul_id>', api_delete_matkul, name="api_delete_matkul"),
]