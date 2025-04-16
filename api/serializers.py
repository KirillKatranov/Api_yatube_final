from rest_framework import serializers

from .models import Follow, Group, Post, Comment, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group')
        read_only_fields = ('owner', 'pub_date', 'author')


class CommentSerializer(serializers.ModelSerializer):
    pass



class GroupSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Group
        fields = ('id', 'title')

class FollowSerializer(serializers.ModelSerializer):
    pass