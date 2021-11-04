from django.forms import ModelForm
from .models import Matakuliah, Jadwal
from django.forms.widgets import Input, Select

class MatkulForm(ModelForm):
  class Meta:
    model = Matakuliah
    fields = ["user", "nama","kelas","SKS"]
    widgets = {
            "user": Input(attrs={"class": "form-control"}),
            "nama": Select(attrs={"class": "form-select"}),
            "kelas": Input(attrs={"class": "form-control", "placeholder":"Masukkan kelas dari mata kuliah tersebut"}),
            "SKS": Input(attrs={"class": "form-control", "placeholder":"Masukkan jumlah SKS dari mata kuliah tersebut"})
        }

class JadwalForm(ModelForm):
  class Meta:
    model = Jadwal
    fields = ["matkul", "hari","start","end"]
    widgets = {
            "matkul": Input(attrs={"class": "form-control"}),
            "hari": Select(attrs={"class": "form-select"}),
            "start": Input(attrs={"class": "form-control", "placeholder":"Harap masukkan input dalam format jj:mm:dd"}),
            "end": Input(attrs={"class": "form-control", "placeholder":"Harap masukkan input dalam format jj:mm:dd"})
        }