from django.shortcuts import render
from schedule_kuliah.models import Matakuliah, Jadwal
from .models import Agenda

# Create your views here.

def index(request):
    agendas = Agenda.objects.all().values()
    response = {'agendas': agendas}
    return render(request, 'agenda_main.html', response)

