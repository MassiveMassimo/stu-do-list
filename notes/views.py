from django.shortcuts import render
from .models import Notes
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import 

def index(request):
  notes = Notes.objects.all()
  response = {'notes': notes}
  return render(request, 'notes_index.html', response)

@login_required(login_url="/admin/login/")
def add_notes(request):
  form = NotesForm(request.POST or None)
  if (form.is_valid() and request.method == 'POST'):
    form.save()
    return HttpResponseRedirect('/notes/')
  context ={'form':form}
  return render(request, "notes_form.html", context)