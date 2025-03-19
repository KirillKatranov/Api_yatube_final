from rest_framework import filters


class FollowingFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(following__username=request.user)
