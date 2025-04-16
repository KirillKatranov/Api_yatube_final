from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='post')
v2_router = DefaultRouter()
v2_router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/',  include(v2_router.urls)),
    path('v1/', include('djoser.urls')),  # Работа с пользователями
    path('v1/', include('djoser.urls.jwt')), #
]
