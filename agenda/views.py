from django.http import response
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from schedule_kuliah.models import Matakuliah, Jadwal
from .models import Agenda
from .forms import AgendaForm
from django.core import serializers

# Create your views here.

# @login_required(login_url="authentication") # Kalo ntar ada object user
def index(request):
    agendas = Agenda.objects.all().values()
    response = {'agendas' : agendas}
    # schedules = Jadwal.objects.all().values()
    # response = {'agendas' : agendas, 'schedules' : schedules}
    return render(request, 'agenda_main.html', response)
    # return (request, 'agenda_main.html')

# kalo ada yg gabener bentar ya ini copas lab kemaren mmmmfffff
@login_required(login_url="/admin/login/") # Kalo yg bisa edit cm admin
# @login_required(login_url="authentication") # Kalo ntar ada object user
def add_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to DB
            return HttpResponseRedirect('/agenda')  # Redirect on finish
        
    else: # if a GET (or any other method) we'll create a blank form
        form = AgendaForm()

    return render(request, 'agenda_form.html', {'form': form})

    # form = AgendaForm()
    # if request.method == "POST":
    #     data = request.POST.dict()
    #     data["user"] = request.user
    #     form = AgendaForm(data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("/contohapp")
    # context = {"form": form}
    # return render(request, "add_todo.html", context)

@login_required(login_url="/admin/login/") # Kalo yg bisa edit cm admin
# @login_required(login_url="authentication") # Kalo ntar ada object user
def get_agenda(request):
    agendas = Agenda.objects.all()
    agendas_json = serializers.serialize("json", agendas)
    return HttpResponse(agendas_json, content_type="application/json")

@login_required(login_url="/admin/login/") # Kalo yg bisa edit cm admin
# @login_required(login_url="authentication") # Kalo ntar ada object user
def delete_agenda(request, agenda_id):
    try:
        Agenda.objects.get(id=agenda_id).delete()
    except Exception as e:
        print(e)
    finally:
        return redirect("/agenda/")