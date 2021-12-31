from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseServerError
from django.shortcuts import render, redirect
from .models import Jadwal, Matakuliah
from .forms import MatkulForm, JadwalForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @login_required(login_url = '/login')


def index(request):
    context = {"user_id": request.user.id}
    return render(request, "schedule_index.html", context)


@login_required(login_url='/login')
def get_jadwal(request, user_id):
    matkuls = Matakuliah.objects.filter(user=user_id)
    jadwals = {}
    for matkul in matkuls:
        # convert Query set (Objects Jadwal hasil filter) menjadi json
        jadwal_json = serializers.serialize(
            "json", Jadwal.objects.filter(matkul=matkul.id))
        # Mengubah json menjadi list python menggunakan json.loads(string_json)
        jadwals[matkul.nama] = {"id": matkul.id, "kelas": matkul.kelas,
                                "sks": matkul.SKS, "jadwal": json.loads(jadwal_json)}
    # Mengubah dict python menjadi json menggunakan json.dumps(dict)
    data = json.dumps(jadwals)
    return HttpResponse(data, content_type="application/json")


@login_required(login_url='/login')
def add_matkul(request):
    context = {}
    if request.method == "POST":
        data_matkul = request.POST.dict()
        print(request.user)
        data_matkul["user"] = request.user.id
        form = MatkulForm(data_matkul)
        print(form.errors)
        found = len(Matakuliah.objects.filter(
            nama=data_matkul["nama"], user=request.user.id)) > 0
        if found:
            nama = data_matkul['nama']
            context["error"] = f"Mata kuliah {nama} sudah pernah ditambahkan"
        elif form.is_valid():
            matkul_created = form.save()
            return redirect("schedule:add_jadwal", matkul_created.id)
        else:
            context["error"] = "Mata kuliah gagal ditambahkan: invalid input"
    form = MatkulForm()
    context.update({"form": form})
    return render(request, "schedule_form_matkul.html", context)


@login_required(login_url='/login')
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
            context["error"] = "Jadwal gagal ditambahkan: invalid input"
    form = JadwalForm()
    context.update({"form": form, "matkul": f"{matkul.nama} - {matkul.kelas}"})
    return render(request, "schedule_form_jadwal.html", context)


@login_required(login_url='/login')
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
        print(e)
    finally:
        return redirect("schedule:index")


@login_required(login_url="main:login")
def delete_matkul(request, matkul_id):
    try:
        matkul = Matakuliah.objects.get(pk=matkul_id)
        matkul.delete()
    except Exception as e:
        print(e)
    finally:
        return redirect("schedule:index")

# API


def api_get_jadwal(request, user_id):
    matkuls = Matakuliah.objects.filter(user=user_id)
    jadwals = {}
    for matkul in matkuls:
        # convert Query set (Objects Jadwal hasil filter) menjadi json
        jadwal_json = serializers.serialize(
            "json", Jadwal.objects.filter(matkul=matkul.id))
        # Mengubah json menjadi list python menggunakan json.loads(string_json)
        jadwals[matkul.nama] = {"id": matkul.id, "kelas": matkul.kelas,
                                "SKS": matkul.SKS, "jadwal": json.loads(jadwal_json)}
    # Mengubah dict python menjadi json menggunakan json.dumps(dict)
    data = json.dumps({
        "status": "success",
        "data": jadwals
    })
    return HttpResponse(data, content_type="application/json")


def api_get_matkul(request, user_id):
    matkuls = serializers.serialize(
        "json", Matakuliah.objects.filter(user=user_id))
    data = json.dumps({
        "status": "success",
        "data": json.loads(matkuls)
    })
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def api_add_matkul(request, user_id):
    context = {}
    if request.method == "POST":
        data_matkul = json.loads(request.body.decode('utf-8'))
        data_matkul["user"] = user_id
        form = MatkulForm(data_matkul)
        found = len(Matakuliah.objects.filter(
            nama=data_matkul["nama"], user=user_id)) > 0
        if found:
            nama = data_matkul['nama']
            context["error"] = f"Mata kuliah {nama} sudah pernah ditambahkan"
        elif form.is_valid():
            matkul_created = form.save()
            context["status"] = "success"
            context["data"] = {"id": matkul_created.id, "nama": matkul_created.nama,
                               "kelas": matkul_created.kelas, "SKS": matkul_created.SKS}
        else:
            context["error"] = "Mata kuliah gagal ditambahkan: invalid input"
        data = json.dumps(context)
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponseNotAllowed()


@csrf_exempt
def api_add_jadwal(request, matkul_id):
    context = {}
    try:
        Matakuliah.objects.get(pk=matkul_id)
    except Exception:
        return HttpResponseBadRequest()
    if request.method == "POST":
        data_jadwal = json.loads(request.body.decode('utf-8'))
        data_jadwal["matkul"] = matkul_id
        print(data_jadwal)
        form = JadwalForm(data_jadwal)
        if form.is_valid():
            form.save()
            context["status"] = "success"
        else:
            context["error"] = "Jadwal gagal ditambahkan: invalid input"
        return HttpResponse(context, content_type="application/json")


def api_delete_jadwal(request, jadwal_id):
    try:
        jadwal = Jadwal.objects.get(pk=jadwal_id)
        jadwal.delete()
        jadwal_sisa = Jadwal.objects.filter(matkul=jadwal.matkul)
        if len(jadwal_sisa) == 0:
            matkul = Matakuliah.objects.get(pk=jadwal.matkul.id)
            matkul.delete()
        return HttpResponse({"status": "success"}, content_type="application/json")
    except Exception as e:
        return HttpResponseServerError()


@csrf_exempt
def api_delete_matkul(request, matkul_id):
    try:
        matkul = Matakuliah.objects.get(pk=matkul_id)
        matkul.delete()
        return HttpResponse({"status": "success"}, content_type="application/json")
    except Exception as e:
        return HttpResponseServerError()
