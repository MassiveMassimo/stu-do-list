from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import JadwalBelajarBareng
from .forms import JadwalForm
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
    # course = request.POST.get("name")
    # # tanggal = request.POST.get("tanggal")
    # waktu = request.POST.get("waktu")
    # topik = request.POST.get("topik")
    # info = request.POST.get("info")
    # link = request.POST.get("link")
    
    # simpan = JadwalBelajarBareng.objects.create(Matkul = course, Waktu = waktu, Topik = topik, Informasi = info, Link = link)
    # simpan.save()
    # name = course
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
def remove_jadwal(request, pk):
  jdwl = JadwalBelajarBareng.objects.get(id = pk)
  if request.method == "POST":
    jdwl.delete()
    return redirect('/jadwal-belajar-bareng')
    
  context = { 'sched' : jdwl }
  return render(request, 'remove_jadwal.html', context)
