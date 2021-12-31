from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import NotesModel
from .forms import NotesForm
from django.core import serializers
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import NotesSerializer


# import get_object_or_404, from django.core import serializers, from django.http.response import HttpResponse

def notes(request):
    datas = NotesModel.objects.all()
    context = {'datas': datas}
    return render(request, 'notes.html', context)


@login_required(login_url='/login')
def add_notes(request):
    form = NotesForm()
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes')

    context = {'form': form}
    return render(request, 'add_notes.html', context)


@login_required(login_url='/login')
def remove_notes(request, id):
    obj = get_object_or_404(NotesModel, id=id)
    if request.method == 'POST':
        obj.delete()
    note = serializers.serialize('json', NotesModel.objects.all())
    return HttpResponse(note, content_type='application/json')
    # if request.method == "POST":
    #     notes_id = request.POST.get('id')
    #     NotesModel.objects.filter(id=notes_id).delete()
    #     return JsonResponse({'status': True})


def detail_notes(request, matkul):
    data = NotesModel.objects.filter(Matkul=matkul)
    datas = NotesModel.objects.all()
    context = {
        'data': data,
        'datas': datas,
    }
    return render(request, 'notes.html', context)


class notes_json(viewsets.ModelViewSet):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer
