from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from schedule_kuliah.models import Matakuliah, Jadwal
from .models import Agenda
from .forms import AgendaForm

# Create your views here.

def index(request):
    agendas = Agenda.objects.all().values()
    schedules = Jadwal.objects.all().values()
    response = {'agendas' : agendas, 'schedules' : schedules}
    return render(request, 'agenda_main.html', response)

# kalo ada yg gabener bentar ya ini copas lab kemaren mmmmfffff
@login_required(login_url="/admin/login/")
def add_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to DB
            return HttpResponseRedirect('/agenda')  # Redirect on finish
        
    else: # if a GET (or any other method) we'll create a blank form
        form = AgendaForm()

    return render(request, 'agenda_form.html', {'form': form})