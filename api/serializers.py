from rest_framework import serializers

from .models import Follow, Group, Post, Comment, User


class PostWriteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('id', 'text', 'group', 'author')


class PostReadSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    group = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group')

class CommentWriteSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author')

class CommentReadSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created', 'post')

class GroupSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Group
        fields = ('id', 'title')

class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    user = serializers.StringRelatedField()
    class Meta:
        model = Follow
        fields = ('id', 'following', 'user')
        read_only_fields = ('user',)
