from django.urls import path
from .views import index, add_community 

urlpatterns = [
  path('', index, name='index'),
  path('add-study-community', add_community, name='add-community')
]