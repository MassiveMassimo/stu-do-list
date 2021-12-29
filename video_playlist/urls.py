from django.urls import path
from .views import get_playlist, index, add_video, flutter_project

urlpatterns = [
  path('', index, name='index'),
  path('add-video', add_video, name='add'),
  path('video-flutter', flutter_project, name='video'),
  path('get-playlist', get_playlist, name='get'),
  
]