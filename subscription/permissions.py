# subscription/permissions.py

from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to modify objects.
    """

    def has_permission(self, request, view):
        # Allow read-only (GET, HEAD, OPTIONS) for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write (POST, PUT, DELETE) only for admin users
        return request.user and request.user.is_authenticated and request.user.is_admin

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin users to modify objects.
    """

    def has_permission(self, request, view):
        # Allow write (POST, PUT, DELETE) only for admin users
        return request.user and request.user.is_authenticated and request.user.is_admin