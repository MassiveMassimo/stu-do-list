from django import forms
from django.forms.widgets import Input
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'type':'text', 'id': 'inputTitle', 'class':'form-control'}),
            'matkul': forms.Select(attrs={'type':'text', 'id': 'inputMatkul', 'class':'form-control'}),
            'message': forms.Textarea(attrs={'type':'text', 'id': 'inputMessage', 'class':'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"