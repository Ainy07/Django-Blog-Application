from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_date']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    num_likes = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'published_date', 'comments', 'num_likes']
