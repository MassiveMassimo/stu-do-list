from django import forms
from django.forms import ModelForm
from .models import Agenda

class AgendaForm(ModelForm):
    class Meta :
        model = Agenda
        fields = ['nama', 'due_date', 'keterangan']
        widgets = {
            'due_date': forms.SelectDateWidget(years=range(2021, 2030))
        }