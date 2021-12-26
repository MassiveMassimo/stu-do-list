from django.urls import path, include
from . import  views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register('community', views.community_json)

urlpatterns = [
  path('', views.index, name='communities'),
  path('add-study-community', views.add_community, name='add-community'),
  path('delete-study-community', views.delete_community, name='delete-community'),
  path('community-json', include(router.urls)),
]