from django.shortcuts import render, redirect
from .models import Community
from .forms import CommunityForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
  community = Community.objects.all()
  response = {'community': community}
  return render(request, 'study_community_index.html', response)

@login_required(login_url = '/login')
def add_community(request):
  form = CommunityForm(request.POST or None)
  if (form.is_valid() and request.method == 'POST'):
    form.save()
    return redirect('/study-communities/')
  context ={'form':form}
  return render(request, "community_form.html", context)

@login_required(login_url = '/login')
def delete_community(request):
  if request.method == "POST":
    community_id = request.POST.get('id')
    Community.objects.filter(id=community_id).delete()
    return JsonResponse({'status':True})