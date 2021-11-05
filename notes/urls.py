from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
  path('', views.notes, name='notes'),
  path('<str:matkul>', views.detail_notes, name='matkul'),
  path('add/', views.add_notes, name='addnotes'),
  path('remove/<str:id>/', views.remove_notes, name ='removenotes'),
]
