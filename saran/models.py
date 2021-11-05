from django.db import models

# Create your models here.

class Saran(models.Model):
  def __str__(self): 
    return self.Nama
  Nama = models.CharField(max_length = 30)
  Email = models.EmailField(max_length = 30)
  Teks = models.TextField()