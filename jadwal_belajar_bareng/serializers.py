from rest_framework import serializers
from .models import JadwalBelajarBareng

class JadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JadwalBelajarBareng
        fields = (
        'id', 
        'Prioritas', 
        'Matkul', 
        'Waktu', 
        'Topik', 
        'Informasi', 
        'Link'
        )