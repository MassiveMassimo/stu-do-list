from django import forms
from .models import NotesModel


class NotesForm(forms.ModelForm):
    class Meta:
        model = NotesModel
        fields = "__all__"
        widgets = {
            'Penulis': forms.TextInput(
                attrs={'type': 'text', 'id': 'inputPenulis', 'placeholder': 'Nama Penulis catatan',
                       'class': 'form-control'}),
            'Matkul': forms.TextInput(attrs={'type': 'text', 'id': 'inputMatkul', 'placeholder': 'Mata Kuliah terkait',
                                             'class': 'form-control'}),
            'Topik': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Topik pembelajaran'}),
            'Keterangan': forms.Textarea(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Keterangan'}),
            'Link': forms.URLInput(attrs={'type': 'url', 'class': 'form-control', 'placeholder': 'Link catatan'})
        }
