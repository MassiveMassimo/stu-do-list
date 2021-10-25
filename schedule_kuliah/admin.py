from django.contrib import admin
from .models import Matakuliah, Dosen, Jadwal

# Register your models here.

admin.site.register(Matakuliah, Dosen)
admin.site.register(Jadwal)