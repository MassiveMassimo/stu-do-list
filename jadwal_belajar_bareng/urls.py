from django.urls import path
from . import views

app_name = 'jadwal'

urlpatterns = [
  path('', views.jadwal, name = 'jadwal'),
  path('add/', views.add_jadwal, name= 'addjadwal'),
  path('remove/<str:pk>/', views.remove_jadwal, name = 'removejadwal'),
  path('json', views.json),
  path('xml', views.xml),
]
