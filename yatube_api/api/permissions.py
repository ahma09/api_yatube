from rest_framework import permissions


class isAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'POST'):
            return request.user.is_authenticated
        return obj.author == request.user
