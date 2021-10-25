from django.db import models

class Community(models.Model):
  nama = models.CharField(max_length=50)
  kelas = models.CharField(max_length=15)
  prodi = models.CharField(max_length=50)
  info = models.CharField(max_length=100)
  link = models.URLField()