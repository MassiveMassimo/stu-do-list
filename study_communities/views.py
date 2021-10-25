from django.shortcuts import render
from .models import Community
from django.http.response import HttpResponseRedirect

def index(request):
  community = Community.objects.all()
  response = {'community': community}
  return render(request, 'student_community_index.html', response)

def add_community(request):
  form = CommunityForm(request.POST or None)
  if (form.is_valid and request.method == 'POST'):
    form.save()
    return HttpResponseRedirect('/study_communities/')
  context ={'form':form}
  return render(request, "community_form.html", context)