from django.urls import path
from . import views

app_name = 'ask_a_mentor'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.add_post, name = 'add_post'),
    path('alin.html/', views.alin, name = 'alin'),
    path('mppi.html/', views.mppi, name = 'mppi'),
    path('pbp.html/', views.pbp, name = 'pbp'),
    path('sda.html/', views.sda, name = 'sda'),
    path('sosi.html/', views.sosi, name = 'sosi'),
]