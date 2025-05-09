from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Follow, Post, Comment, Group, User
from .serializers import (CommentReadSerializer, CommentWriteSerializer, PostReadSerializer, 
                          GroupSerializer, FollowSerializer, PostWriteSerializer)
from .permissions import OwnerOrReadOnly



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (OwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostReadSerializer
        return PostWriteSerializer

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_id)
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CommentReadSerializer
        return CommentWriteSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_id)
        if post.author != self.request.user:
            return Response({"detail": "You do not have permission to edit this post."}, status=403)
        serializer.save(author=self.request.user, post=post)
    


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerOrReadOnly,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username',)

    def get_queryset(self):
        return Follow.objects.filter(following__username=self.request.user.username)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["following"]
        exist_object = Follow.objects.filter(user=request.user, following__username=username)
        if exist_object:
            return Response(data="Такая подписка уже есть", status=400)
        following_user = get_object_or_404(User, username=username)
        if request.user == following_user:
            return Response(data="На себя подписываться нельзя", status=400)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
