from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

# Create your views here.
def index(request):
  video_playlist = Video.objects.all()
  response = {"video_playlist" : video_playlist}
  return render(request, "video_playlist.html", response)

@login_required(login_url='/login')
def add_video(request):
  response = {}
  form = VideoForm(request.POST)
  if request.method == 'POST':
    title = request.POST.get('title')
    link = request.POST.get('link')

    new_video = Video(
      Title = title,
      Link = link
    )

    new_video.save()

    return HttpResponseRedirect('')

  response['form']= form
  return render(request, "video_playlist_form.html", response)

@csrf_exempt
def flutter_project(request):
  if request.method == 'POST':
        videoPlaylist = json.loads(request.body)

        new_video = Video(
            Title = videoPlaylist['title'],
            Link = videoPlaylist['link'],
        )

        new_video.save()
        return JsonResponse({"instance": "Video berhasil ditambahkan!"}, status=200)

def get_playlist(request):
    video_playlist = Video.objects.all()
    data = serializers.serialize('json', video_playlist)
    response = {
            'video_playlist':data,
            }
    return JsonResponse(response)

