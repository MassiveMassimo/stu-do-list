from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import Saran
from .forms import SaranForm
from django.core import serializers
from django.http.response import HttpResponse 
from django.contrib.auth.decorators import login_required

def saran(request):
  saran = Saran.objects.all()
  context = { 'saran' : saran }
  return render(request, 'jadwal_belajar_bareng.html', context)

def add_jadwal(request):
  form = SaranForm()
  if request.method == "POST":
    form = SaranForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/jadwal-belajar-bareng')
  
  context = {'form' : form }
  return render(request, 'add_jadwal.html', context)