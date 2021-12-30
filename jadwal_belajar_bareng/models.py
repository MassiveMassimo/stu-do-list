from django.db import models

CHOICES = (
  ("Alin","Alin"),
  ("MPPI","MPPI"),
  ("PBP","PBP"),
  ("SOSI","SOSI"),
  ("SDA","SDA"),
)

PRIORITY = (
  ("Tinggi","Tinggi"),
  ("Sedang","Sedang"),
  ("Rendah","Rendah"),
)

class JadwalBelajarBareng(models.Model):
  def __str__(self): 
    return self.Topik
  Prioritas = models.TextField(max_length = 15, choices=PRIORITY)
  Matkul = models.TextField(max_length = 150, choices=CHOICES)
  Waktu = models.CharField(max_length = 150)
  Topik = models.CharField(max_length = 150)
  Informasi = models.TextField()
  Link = models.CharField(max_length = 200)