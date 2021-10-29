from django.urls import path
from . import  views

urlpatterns = [
  path('', views.index, name='communities'),
  path('add-study-community', views.add_community, name='add-community'),
  path('delete-study-community', views.delete_community, name='delete-community')
]