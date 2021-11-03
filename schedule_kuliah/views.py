from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import Jadwal, Matakuliah
from .forms import MatkulForm, JadwalForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
# Create your views here.

 
def index(request):
    context = {"user_id": request.user.id}
    return render(request, "schedule_index.html", context)


def get_jadwal(request, user_id):
    matkuls = Matakuliah.objects.filter(user=user_id)
    jadwals = {}
    for matkul in matkuls:
        # convert Query set (Objects Jadwal hasil filter) menjadi json
        jadwal_json = serializers.serialize("json", Jadwal.objects.filter(matkul=matkul.id))
        # Mengubah json menjadi list python menggunakan json.loads(string_json)
        jadwals[matkul.nama] = {"id": matkul.id, "jadwal": json.loads(jadwal_json)}
    # Mengubah dict python menjadi json menggunakan json.dumps(dict)
    data = json.dumps(jadwals)
    return HttpResponse(data, content_type="application/json")


@login_required(login_url="/admin/login")
def add_matkul(request):
    if request.method == "POST":
        data_matkul = request.POST.dict()
        print(request.user)
        data_matkul["user"] = request.user.id
        form = MatkulForm(data_matkul)
        print(form.errors)
        if form.is_valid():
            matkul_created = form.save()
            return redirect("schedule:add_jadwal", matkul_created.id)
        print("Data yang disubmit tidak valid")
    form = MatkulForm()
    context = {"form": form}
    return render(request, "schedule_form_matkul.html", context)


def add_jadwal(request, matkul_id):
    print('masuk add jadwal')
    context = {}
    try:
        matkul = Matakuliah.objects.get(pk=matkul_id)
    except Exception:
        return redirect("schedule:index")
    if request.method == "POST":
        data_jadwal = request.POST.dict()
        data_jadwal["matkul"] = matkul_id
        form = JadwalForm(data_jadwal)
        if form.is_valid():
            form.save()
            context["info"] = "Jadwal berhasil ditambahkan"
        else:
            context["error"] = "Jadwal yang dimasukkan invalid"
    form = JadwalForm()
    context.update({"form": form, "matkul": f"{matkul.nama} - {matkul.kelas}"})
    return render(request, "schedule_form_jadwal.html", context)


def delete_jadwal(request, jadwal_id):
    try:
        jadwal = Jadwal.objects.get(pk=jadwal_id)
        jadwal.delete()
        jadwal_sisa = Jadwal.objects.filter(matkul=jadwal.matkul)
        print(jadwal_sisa)
        print(len(jadwal_sisa))
        if len(jadwal_sisa) == 0:
            matkul = Matakuliah.objects.get(pk=jadwal.matkul.id)
            matkul.delete()
    except Exception as e:
        print (e)
    finally:
        return redirect("schedule:index")