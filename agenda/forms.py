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
            'matkul' : Select(attrs={"class": "form-control"}, choices=KODEMATKUL),
            'judul' : Input(attrs={"class": "form-control"}),
            'tanggal' : DateInput(attrs={"class": "form-control"}),
            'waktu' : TimeInput(attrs={'type': 'time', "class": "form-control"}),
            'keterangan' : Textarea(attrs={"class": "form-control"}),
        }