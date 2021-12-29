from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'jadwal'

router = routers.DefaultRouter(trailing_slash = False)
router.register('/jadwal', views.jadwal_belajar_json)

urlpatterns = [
  path('', views.jadwal, name = 'jadwal'),
  path('add/', views.add_jadwal, name= 'addjadwal'),
  path('remove/<str:id>/', views.remove_jadwal, name = 'removejadwal'),
  path('edit/<str:id>/', views.edit_jadwal, name = 'editjadwal'),
  path('json', views.json),
  path('xml', views.xml),
  path('jadwal-belajar-json', include(router.urls)),
  path('prioritas_tinggi.html/', views.prioritas_tinggi, name='prioritas_tinggi'),
  path('prioritas_sedang.html/', views.prioritas_sedang, name='prioritas_sedang'),
  path('prioritas_rendah.html/', views.prioritas_rendah, name='prioritas_rendah'),
  path('prioritas_all.html/', views.prioritas_all, name='prioritas_all'),
]
