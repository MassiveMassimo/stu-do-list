from django.forms import ModelForm
from .models import Matakuliah, Dosen, Jadwal

class MatkulForm(ModelForm):
  class Meta:
    model = Matakuliah
    fields = ["nama","kelas","dosen","SKS"]