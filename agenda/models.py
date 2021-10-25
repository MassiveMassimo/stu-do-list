from django.db import models

# Create your models here.
class Agenda(models.Model) :
  nama = models.CharField(max_length=200)
  due_date = models.DateField()
  keterangan = models.TextField()