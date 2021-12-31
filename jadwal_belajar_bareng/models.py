from django.db import models

class JadwalBelajarBareng(models.Model):
  def __str__(self): 
    return self.Topik
  Prioritas = models.TextField(max_length = 15)
  Matkul = models.TextField(max_length = 150)
  Waktu = models.CharField(max_length = 150)
  Topik = models.CharField(max_length = 150)
  Informasi = models.TextField()
  Link = models.CharField(max_length = 200)