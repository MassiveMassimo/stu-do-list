from django.shortcuts import render, redirect
from .models import Matakuliah, Dosen, Jadwal
from .forms import MatkulForm
# Create your views here.

def index(request):
  jadwal = Jadwal.objects.all()
  response = {"jadwal" : jadwal}
  return render(request, "schedule_index.html", response)

@login_required(login_url="/admin/login/")
def add_matkul(request):
  if request.method == "POST"
    form = MatkulForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect ("schedule:schedule_form_jadwal")
    print("Data yang disubmit tidak valid")
  form = MatkulForm()
  context = {"form" : form}
  return render(request, "schedule_form.html",context)

@login_required(login_url="/admin/login/")
def add_schedule(request):
  if request.method == "POST"
    form = 
