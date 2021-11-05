from django import forms
from django.forms import ModelForm
from .models import Agenda, KODEMATKUL
from django.forms.widgets import Input, Select, Textarea, TimeInput

class DateInput(forms.DateInput):
    input_type = 'date'

class AgendaForm(ModelForm):
    class Meta :
        model = Agenda
        fields = ['matkul', 'judul', 'tanggal', 'waktu', 'keterangan']
        widgets = {
            # 'matkul' : forms.Select(attrs={"class": "form-control"}, choices=KODEMATKUL),
            'matkul' : forms.Select(attrs={"class": "form-control"}),
            'judul' : forms.Input(attrs={"class": "form-control"}),
            'tanggal' : forms.DateInput(attrs={"class": "form-control"}),
            'waktu' : forms.TimeInput(attrs={'type': 'time', "class": "form-control"}),
            'keterangan' : forms.Textarea(attrs={"class": "form-control  text-dim"}),
        }