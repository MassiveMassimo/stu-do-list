from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('notes', views.notes_json)

app_name = 'notes'

urlpatterns = [
    path('', views.notes, name='notes'),
    path('<str:matkul>', views.detail_notes, name='detail-notes'),
    path('add-notes/', views.add_notes, name='add-notes'),
    path('remove-notes/<id>', views.remove_notes, name='remove-notes'),
    path('notes-json', include(router.urls)),

]
