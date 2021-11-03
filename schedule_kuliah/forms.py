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
            "kelas": Input(attrs={"class": "form-control"}),
            "SKS": Input(attrs={"class": "form-control"})
        }

class JadwalForm(ModelForm):
  class Meta:
    model = Jadwal
    fields = ["matkul", "hari","start","end"]
    widgets = {
            "matkul": Input(attrs={"class": "form-control"}),
            "hari": Select(attrs={"class": "form-select"}),
            "start": Input(attrs={"class": "form-control"}),
            "end": Input(attrs={"class": "form-control"})
        }