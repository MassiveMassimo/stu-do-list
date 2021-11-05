from .models import Community
from django.forms import ModelForm
from django import forms

class CommunityForm(ModelForm):
  class Meta:
    model = Community
    fields = "__all__"
    widgets = {
      'nama': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan nama mata kuliah'}),
      'kelas': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan kelas'}),
      'prodi': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan program studi'}),
      'info': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan keterangan tambahan'}),
      'link': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'placeholder':'Masukkan link grup'})
    }