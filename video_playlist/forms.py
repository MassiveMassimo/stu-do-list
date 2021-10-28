from django.forms import ModelForm
from .models import Video
from django import forms

class VideoForm(ModelForm):
  class Meta:
    model = Video
    fields = "__all__"
    widgets = {
      'Title': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'title', 'placeholder':'Enter title', 'name':'title'}),
      'Link': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'link', 'placeholder':'Enter embedded link', 'name':'link'}),
    }