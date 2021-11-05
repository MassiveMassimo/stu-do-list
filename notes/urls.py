from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes, name='notes'),
    path('<str:matkul>', views.detail_notes, name='detail-notes'),
    path('add-notes/', views.add_notes, name='add-notes'),
    path('remove-notes/<id>', views.remove_notes, name='remove-notes'), #add parameter to url
]
