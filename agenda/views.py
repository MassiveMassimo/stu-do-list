from django.http import response
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from schedule_kuliah.models import Matakuliah, Jadwal
from .models import Agenda
from .forms import AgendaForm
from django.core import serializers

# Create your views here.

@login_required(login_url = '/login')
def index(request):
    # agendas = Agenda.objects.all().values()
    # response = {'agendas' : agendas}
    # return render(request, 'agenda_main.html', response)
  
    context = {"user_id": request.user.id}
    return render(request, "agenda_main.html", context)

@login_required(login_url = '/login')
def add_agenda(request):
    if request.method == 'POST':
        agendas = request.POST.dict()
        print(request.user)
        agendas["user"] = request.user.id
        form = AgendaForm(agendas)
        if form.is_valid():
            agenda_created = form.save()  # Save data to DB
            return redirect("agenda:index", agenda_created.id)
            # return redirect('/agenda')  # Redirect on finish
    form = AgendaForm()
    return render(request, "agenda_form.html", {"form": form})
    # else: # if a GET (or any other method) we'll create a blank form
    #     form = AgendaForm()
    # return render(request, 'agenda_form.html', {'form': form})

@login_required(login_url = '/login')
def get_agenda(request, user_id):
    # agendas = Agenda.objects.all()
    agendas = Agenda.objects.filter(user=user_id)
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