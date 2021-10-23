from django.db import models

Kode_Matkul = [
  ("Alin"),
  ("Basdat")
  ("Manpro"),
  ("MPPI"),
]

class Matakuliah (models.Model):
  kode = models.CharField(max_length=10)
  kelas = models.CharField(max_length=1)
  jadwal = models.