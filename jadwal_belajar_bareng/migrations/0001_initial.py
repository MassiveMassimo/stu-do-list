# Generated by Django 3.2.9 on 2021-11-03 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JadwalBelajarBareng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prioritas', models.TextField(choices=[('Tinggi', 'Tinggi'), ('Sedang', 'Sedang'), ('Rendah', 'Rendah')], max_length=15)),
                ('Matkul', models.TextField(choices=[('Alin', 'Aljabar Linear'), ('MPPI', 'Metodologi Penelitian dan Penulisan Ilmiah'), ('PBP', 'Pemrograman Berbasis Platform'), ('SOSI', 'Sistem Operasi untuk Sistem Informasi'), ('SDA', 'Struktur Data & Algoritma')], max_length=150)),
                ('Waktu', models.DateTimeField()),
                ('Topik', models.CharField(max_length=150)),
                ('Informasi', models.TextField()),
                ('Link', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]