from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import NotesModel
from .forms import NotesForm
from django.contrib.auth.decorators import login_required


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


# @login_required(login_url='/login')
def remove_notes(request, id):
    note = NotesModel.objects.get(id=id)
    if request.method == "POST":
        note.delete()
        return redirect('/notes')

    context = {'note': note}
    return render(request, 'remove_notes.html', context)


def detail_notes(request, matkul):
    data = NotesModel.objects.filter(Matkul=matkul)
    datas = NotesModel.objects.all()
    context = {
        'data': data,
        'datas': datas,
    }
    return render(request, 'notes.html', context)
