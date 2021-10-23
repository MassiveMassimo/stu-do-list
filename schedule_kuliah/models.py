from django.db import models

KODEMATKUL = (
  ("Alin","Aljabar Linear"),
  ("MPPI","Metodologi Penelitian dan Penulisan Ilmiah"),
  ("PBP","Pemrograman Berbasis Platform"),
  ("SOSI","Sistem Operasi untuk Sistem Informasi"),
  ("SDA","Struktur Data & Algoritma"),
)

HARI = (
  ("Senin","Senin"),
  ("Selasa","Selasa"),
  ("Rabu","Rabu"),
  ("Kamis","Kamis"),
  ("Jumat","Jumat"),
)

#Buat ngetest doang pake charfield dulu semua deh <3

class Matakuliah(models.Model):
  nama = models.CharField(max_length=200,choices=KODEMATKUL)
  kelas = models.CharField(max_length=1)
  SKS = models.CharField(max_length=1)

  def _str_ (self):
    return self.nama

class Dosen(models.Model):
  matkul = models.ForeignKey(Matakuliah, null=True) # One to Many
  nama = models.CharField(max_length=100)
  nomor_telepon = models.CharField(max_length=13)
  email = models.CharField(max_length=100)

  def _str_ (self):
    return self.nama

class Jadwal(models.Model):
  matkul = models.ForeignKey(Matakuliah, null=True) # One to Many
  hari = models.CharField(max_length=10, choices=HARI)
  start = models.CharField(max_length=10)
  end = models.charfield(max_length=10)