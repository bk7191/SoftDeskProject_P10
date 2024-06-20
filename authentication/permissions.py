from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    pass


# definit permission pour utilisateurs authentifies
class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_superuser
        )


class IsCreationAndIsStaff(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" or request.method == "PUT" or request.method == "PATCH":
            return request.user and request.user.is_staff and request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.user.is_staff:
            return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class IsTheUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_authenticated)
