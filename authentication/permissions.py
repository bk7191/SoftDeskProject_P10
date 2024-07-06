from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

from projects.models import Contributor


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        return bool(
            request.user or request.user.is_authenticated or request.user.is_staff
        )


# definit permission pour admin authentifies
class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_superuser
        )


class ContributorPermission(BasePermission):
    """
    only allow contributors of a project to view or create
    """

    def has_object_permission(self, request, view, obj):
        return Contributor.objects.filter(project=obj, user=request.user).exists()


class IsCreationAndIsStaff(BasePermission):
    def has_permission(self, request, view):
        if (
                request.method == "GET"
                or request.method == "PUT"
                or request.method == "PATCH"
        ):
            return (
                    request.user and request.user.is_staff and request.user.is_authenticated
            )
        return True

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return False
        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return True
        return bool(
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
        )


class IsStaffPermission(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        if not request.user.is_staff:
            return True
        return super().has_permission(request, view)

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }
