from django.db import models

# Create your models here.
from django.db import models

class Notes(models.Model):
  nama = models.CharField(max_length=50)
  kelas = models.CharField(max_length=15)
  prodi = models.CharField(max_length=50)
  info = models.CharField(max_length=100)
  link = models.URLField()