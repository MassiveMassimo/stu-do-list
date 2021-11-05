from django.db import models


class NotesModel(models.Model):
    Penulis = models.CharField(max_length=150)
    Matkul = models.CharField(max_length=150)
    Topik = models.CharField(max_length=150)
    Keterangan = models.TextField()
    Link = models.URLField(max_length=200)
