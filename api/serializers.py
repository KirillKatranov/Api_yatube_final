from rest_framework import serializers

from .models import Follow, Group, Post, Comment, User


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'group')


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    group = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group')

class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text')

class CommentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'posts','created')

class GroupSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Group
        fields = ('id', 'title')

class FollowSerializer(serializers.ModelSerializer):
    pass
