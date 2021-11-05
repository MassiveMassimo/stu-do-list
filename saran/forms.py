from django import forms
from .models import Saran

class SaranForm(forms.ModelForm):
    class Meta:
        model = Saran
        fields = "__all__"
        widgets = {
            'Nama': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan nama atau inisial Anda'}),
            'Email': forms.EmailInput(attrs={'type':'email', 'class':'form-control', 'placeholder':'Masukkan email Anda'}),
            'Teks': forms.Textarea(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan saran'})
        }