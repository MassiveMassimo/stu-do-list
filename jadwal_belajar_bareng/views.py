from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import JadwalBelajarBareng
from .forms import JadwalForm
from django.core import serializers
from django.http.response import HttpResponse 
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
def jadwal(request):
  jadwalb = JadwalBelajarBareng.objects.all()
  context = { 'jadwalb' : jadwalb }
  return render(request, 'jadwal_belajar_bareng.html', context)

# @login_required
def add_jadwal(request):
  # name = "nama"
  form = JadwalForm()
  if request.method == "POST":
    form = JadwalForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/jadwal-belajar-bareng')
  
  context = {'form' : form }
  return render(request, 'add_jadwal.html', context)

# @login_required
def simpan_jadwal(request):
  return HttpResponseRedirect('/jadwal-belajar-bareng')

# @login_required  
def remove_jadwal(request, id):
  jdwl = JadwalBelajarBareng.objects.get(id = id)
  if request.method == "POST":
    jdwl.delete()
    return redirect('/jadwal-belajar-bareng')
    
  context = { 'sched' : jdwl }
  return render(request, 'remove_jadwal.html', context)

# @login_required  
def edit_jadwal(request, id):
  jdwl = JadwalBelajarBareng.objects.get(id = id)
  if request.method == "POST":
    Prioritas = request.POST.get("Prioritas")
    Matkul = request.POST.get("Matkul")
    Waktu = request.POST.get("Waktu")
    Topik = request.POST.get("Topik")
    Informasi = request.POST.get("Informasi")
    Link = request.POST.get("Link")
    
    simpan = JadwalBelajarBareng.objects.filter(id = id).update(Prioritas = Prioritas, Matkul = Matkul, Waktu = Waktu, Topik = Topik, Informasi = Informasi, Link = Link)
    return redirect('/jadwal-belajar-bareng')
  
  context = { 'sched' : jdwl }
  return render(request, 'edit_jadwal.html', context)

def xml(request):
    data = serializers.serialize('xml', JadwalBelajarBareng.objects.all())
    return HttpResponse(data, content_type="application/xml")

def json(request):
    data = serializers.serialize('json', JadwalBelajarBareng.objects.all())
    return HttpResponse(data, content_type="application/json")