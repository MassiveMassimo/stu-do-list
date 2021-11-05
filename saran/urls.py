from django.urls import path
from . import views

app_name = 'saran'

urlpatterns = [
  path('', views.saran, name = 'saran'),
  path('add/', views.add_saran, name= 'addsaran'),
]