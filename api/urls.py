from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet, basename='post')
group_router = DefaultRouter()
group_router.register(r'group', GroupViewSet, basename='groups')

comment_router = routers.NestedDefaultRouter(post_router, r'posts', lookup='post')
comment_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('v1/', include(post_router.urls)),
    path('v1/',  include(group_router.urls)),
    path('v1/',  include(comment_router.urls)),
    path('v1/', include('djoser.urls')),  # Работа с пользователями
    path('v1/', include('djoser.urls.jwt')), #
]
