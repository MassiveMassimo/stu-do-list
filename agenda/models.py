import datetime
from django.db import models

# from django.contrib.auth.models import User

KODEMATKUL = (
  ("Alin","Aljabar Linear"),
  ("MPPI","Metodologi Penelitian dan Penulisan Ilmiah"),
  ("PBP","Pemrograman Berbasis Platform"),
  ("SOSI","Sistem Operasi untuk Sistem Informasi"),
  ("SDA","Struktur Data & Algoritma"),
)

# Create your models here.
class Agenda(models.Model) :
    # Kalo ada user yg jadi object => yg udah pada login
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    matkul = models.CharField(max_length=200,choices=KODEMATKUL)
    judul = models.CharField(max_length=80)
    tanggal = models.DateField(blank=True, null=True, default=datetime.date.today)
    waktu = models.TimeField(default='23:55')
    keterangan = models.TextField()

    # def __str__(self):
    #     return f"{self.user.username} | {self.judul}"
