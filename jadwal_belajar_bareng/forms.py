from django import forms
from .models import JadwalBelajarBareng
import datetime

class DateTimeInput(forms.DateTimeInput):
    input_type: 'datetime-local'

class JadwalForm(forms.ModelForm):
    class Meta:
        model = JadwalBelajarBareng
        fields = "__all__"
        widgets = {
            'Prioritas': forms.Select(attrs={'type':'text', 'id': 'inputPrioritas', 'class':'form-control'}),
            'Matkul': forms.Select(attrs={'type':'text', 'id': 'inputMatkul', 'class':'form-control'}),
            'Waktu': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'}),
            'Topik': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Topik pembelajaran'}),
            'Informasi': forms.Textarea(attrs={'type':'text', 'class':'form-control', 'placeholder':'Informasi tambahan'}),
            'Link': forms.URLInput(attrs={'type':'url', 'class':'form-control', 'placeholder':'Link pembelajaran daring'})
        }