from django.urls import path
from .views import index, add_notes

urlpatterns = [
  path('', index, name='index'),
  path('add-notes', add_notes, name='add-notes')
]