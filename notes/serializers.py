from rest_framework import serializers

from .models import NotesModel


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        fields = ('id', 'Penulis', 'Matkul', 'Topik', 'Keterangan', 'Link')
