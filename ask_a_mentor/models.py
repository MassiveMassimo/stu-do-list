from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

KODEMATKUL = (
  ("Alin","Aljabar Linear"),
  ("MPPI","Metodologi Penelitian dan Penulisan Ilmiah"),
  ("PBP","Pemrograman Berbasis Platform"),
  ("SDA","Struktur Data & Algoritma"),
  ("SOSI","Sistem Operasi untuk Sistem Informasi"),
)

class Post(models.Model):
    title = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    matkul = models.CharField(max_length=200,choices=KODEMATKUL)
    message = models.CharField(max_length=1000)
    time = models.DateTimeField(default=now, editable=False)
    def __str__ (self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', default='hello')
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    comment = models.CharField(max_length=1000)
    time = models.DateTimeField(default=now, editable=False)
    def __str__ (self):
        return self.user
