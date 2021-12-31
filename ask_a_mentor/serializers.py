from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    read_only = True
    slug_field='username'
    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'matkul', 'message', 'time') 


class CommentSerializer(serializers.ModelSerializer):
    read_only = True
    slug_field='username'
    class Meta:
        model = Comment
        fields = ('id', 'post', 'user', 'comment', 'time') 