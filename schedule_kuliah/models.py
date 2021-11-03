from django.db import models
from django.contrib.auth.models import User

KODEMATKUL = (
  ("Alin","Aljabar Linear"),
  ("MPPI","Metodologi Penelitian dan Penulisan Ilmiah"),
  ("PBP","Pemrograman Berbasis Platform"),
  ("SOSI","Sistem Operasi untuk Sistem Informasi"),
  ("SDA","Struktur Data & Algoritma"),
)

HARI = (
  ("Senin","Senin"),
  ("Selasa","Selasa"),
  ("Rabu","Rabu"),
  ("Kamis","Kamis"),
  ("Jumat","Jumat"),
)

#Buat ngetest doang pake charfield dulu semua deh <3

class Matakuliah(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  nama = models.CharField(max_length=200,choices=KODEMATKUL)
  kelas = models.CharField(max_length=1)
  SKS = models.IntegerField(max_length=1)

  def __str__ (self):
    return self.nama

class Jadwal(models.Model):
  matkul = models.ForeignKey(Matakuliah, on_delete=models.CASCADE) # One to Many
  hari = models.CharField(max_length=10, choices=HARI)
  start = models.TimeField()
  end = models.TimeField()

  def __str__ (self):
    return f"{self.matkul} | {self.hari}"