from django import forms
from django.forms import ModelForm
from .models import Agenda, KODEMATKUL
from django.forms.widgets import Input, Select, Textarea, TimeInput

class AgendaForm(ModelForm):
    class Meta :
        model = Agenda
        fields = ['matkul', 'judul', 'tanggal', 'waktu', 'keterangan']
        widgets = {
            'matkul' : forms.Select(attrs={"class": "form-control"}),
            'judul' : forms.TextInput(attrs={"class": "form-control"}),
            'tanggal' : forms.DateInput(attrs={'type':'date', "class": "form-control"}),
            'waktu' : forms.TimeInput(attrs={'type': 'time', "class": "form-control"}),
            'keterangan' : forms.Textarea(attrs={"class": "form-control  text-dim"}),
        }