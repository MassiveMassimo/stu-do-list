from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
  video_playlist = Video.objects.all()
  response = {"video_playlist" : video_playlist}
  return render(request, "video_playlist.html", response)

@login_required(login_url="/admin/login/")
def add_video(request):
  response = {}
    form = VideoForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return HttpResponseRedirect('/video-playlist/')

    response['form']= form
    return render(request, "video_playlist_form.html", response)

