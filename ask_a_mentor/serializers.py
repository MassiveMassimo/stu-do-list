from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField( source="user.username", read_only=True)
    class Meta:
        model = Post
        fields = '__all__' 
        ezxclude = ('user', )


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField( source="user.username", read_only=True)
    class Meta:
        model = Comment
        exclude = ('user', )