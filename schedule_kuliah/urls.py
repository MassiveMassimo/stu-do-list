from django.urls import path
from .views import index, add_matkul

module_name = "schedule"

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_matkul, name='add_matkul'),
]