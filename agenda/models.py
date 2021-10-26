from django.db import models

KODEMATKUL = (
  ("Alin","Aljabar Linear"),
  ("MPPI","Metodologi Penelitian dan Penulisan Ilmiah"),
  ("PBP","Pemrograman Berbasis Platform"),
  ("SOSI","Sistem Operasi untuk Sistem Informasi"),
  ("SDA","Struktur Data & Algoritma"),
)

# Create your models here.
class Agenda(models.Model) :
  matkul = models.CharField(max_length=200,choices=KODEMATKUL)
  judul = models.CharField(max_length=80)
  tanggal = models.DateField()
  waktu = models.TimeField()
  keterangan = models.TextField()