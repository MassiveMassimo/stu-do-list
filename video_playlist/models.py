from django.db import models

# Create your models here.
class Video(models.Model):
  Title = models.CharField(max_length=100)
  Link = models.URLField()
