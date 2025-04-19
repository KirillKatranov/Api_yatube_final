from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Follow, Post, Comment, Group
from .serializers import (CommentReadSerializer, CommentWriteSerializer, PostReadSerializer, 
                          GroupSerializer, FollowSerializer, PostWriteSerializer)



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostReadSerializer
        return PostWriteSerializer

    
    def create(self, request):
        SerializerClass = self.get_serializer_class()
        serializer: PostWriteSerializer = SerializerClass(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CommentReadSerializer
        return CommentWriteSerializer

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id)#?
        SerializerClass = self.get_serializer_class()
        serializer: CommentWriteSerializer = SerializerClass(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, post=post)#?
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    pass
