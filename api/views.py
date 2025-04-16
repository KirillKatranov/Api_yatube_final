from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Follow, Post, Comment, Group
from .serializers import (PostSerializer, CommentSerializer,
                          GroupSerializer, FollowSerializer)



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    



class CommentViewSet(viewsets.ModelViewSet):
    pass


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    pass
