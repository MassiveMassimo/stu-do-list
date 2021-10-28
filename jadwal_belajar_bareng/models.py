from django.db import models
import datetime
from django.utils.timezone import now
# from django.contrib.auth.models import User

# Create your models here.
CHOICES = (
  ("Alin","Aljabar Linear"),
  ("MPPI","Metodologi Penelitian dan Penulisan Ilmiah"),
  ("PBP","Pemrograman Berbasis Platform"),
  ("SOSI","Sistem Operasi untuk Sistem Informasi"),
  ("SDA","Struktur Data & Algoritma"),
)
class JadwalBelajarBareng(models.Model):
  def __str__(self): 
    return self.Topik
  # user = models.ForeignKey(User, on_delete=models.CASCADE)
  Matkul = models.TextField(max_length = 150, choices=CHOICES)
  # Tanggal = models.DateField(default = datetime.date.today)
  Waktu = models.DateTimeField()
  Topik = models.CharField(max_length = 150)
  Informasi = models.TextField()
  Link = models.URLField(max_length = 200)