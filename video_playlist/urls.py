from django.urls import path
from .views import index, add_video

urlpatterns = [
  path('', index, name='index'),
  path('add-video', add_video, name='add'),
]