from django.http import response
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
# from schedule_kuliah.models import Matakuliah, Jadwal
from .models import Agenda
from .forms import AgendaForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# @login_required(login_url = '/login')
def index(request):
    context = {"user_id": request.user.id}
    return render(request, "agenda_main.html", context)

@login_required(login_url = '/login')
def add_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to DB
            return HttpResponseRedirect('/agenda')  # Redirect on finish
        
    else: # if a GET (or any other method) we'll create a blank form
        form = AgendaForm()

    return render(request, 'agenda_form.html', {'form': form})

# @login_required(login_url = '/login')
def get_agenda(request):
    agendas = Agenda.objects.all()
    agendas_json = serializers.serialize("json", agendas)
    return HttpResponse(agendas_json, content_type="application/json")

@login_required(login_url = '/login')
def delete_agenda(request, agenda_id):
    try:
        Agenda.objects.get(id=agenda_id).delete()
    except Exception as e:
        print(e)
    finally:
        return redirect("/agenda/")

@csrf_exempt
def flutter_add(request):
  if request.method == 'POST':
        agendas = json.loads(request.body)

        new_agenda = Agenda(
            matkul = agendas['matkul'],
            judul = agendas['judul'],
            tanggal = agendas['tanggal'],
            waktu = agendas['waktu'],
            keterangan = agendas['keterangan'],
        )

        new_agenda.save()
        return JsonResponse({"instance": "Agenda berhasil ditambahkan!"}, status=200)