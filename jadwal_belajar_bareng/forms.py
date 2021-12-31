from django import forms
from .models import JadwalBelajarBareng

class JadwalForm(forms.ModelForm):
    class Meta:
        model = JadwalBelajarBareng
        fields = "__all__"
        widgets = {
            'Prioritas': forms.TextInput(attrs={'type':'text', 'id': 'inputPrioritas', 'class':'form-control', 'placeholder':'Tinggi/Sedang/Rendah'}),
            'Matkul': forms.TextInput(attrs={'type':'text', 'id': 'inputMatkul', 'class':'form-control', 'placeholder':'Masukkan mata kuliah'}),
            'Waktu': forms.TextInput(attrs={'type':'text', 'id': 'inputDate', 'class':'form-control', 'placeholder':'Masukkan waktu pembelajaran'}),
            'Topik': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan topik pembelajaran'}),
            'Informasi': forms.Textarea(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan informasi tambahan'}),
            'Link': forms.URLInput(attrs={'type':'url', 'class':'form-control', 'placeholder':'Masukkan situs pertemuan daring'})
        }