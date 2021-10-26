from django import forms
from django.forms import ModelForm
from .models import Agenda

class DateInput(forms.DateInput):
    input_type = 'date'

class AgendaForm(ModelForm):
    class Meta :
        model = Agenda
        fields = ['matkul', 'judul', 'tanggal', 'waktu', 'keterangan']
        widgets = {
            # 'due_date': forms.SelectDateWidget(years=range(2021, 2030))
            'tanggal' : DateInput()
        }