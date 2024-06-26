from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Contributor
from issues.models import Issue


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return obj.author == request.user


class IsProjectContributorAuthenticated(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == "POST":
            project_contributors = [
                user.user_id
                for user in Contributor.objects.filter(
                    project_id=validated_data["project_id"]
                )
            ]
            if request.user.id in project_contributors:
                return True
            else:
                raise PermissionDenied(
                    "You must be contributing to this project to do this"
                )
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        project_contributors = [
            user.user_id for user in Contributor.objects.filter(project_id=obj.id)
        ]
        if isinstance(obj, Issue):
            project_contributors.extend(
                user.user_id
                for user in Contributor.objects.filter(project_id=obj.project)
            )

        return request.user.id in project_contributors


class CanManageProjectContributors(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            contributing_to = [
                project.project_id
                for project in Contributor.objects.filter(user_id=request.user.id)
            ]

            if obj.project.id in contributing_to:
                return True
            else:
                raise PermissionDenied(
                    "You must be contributing to this project to do this"
                )
        elif request.method in SAFE_METHODS:
            return request.user.is_authenticated


class SignupViewPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class IsAuthor(BasePermission):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsContributor(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":  # si il veut creer issue dans projet
            project_id = request.data.get("projet")
            current_user = request.user

    def has_object_permission(self, request, view, obj):

        if request.method == "DELETE":
            if isinstance(obj, Issue):
                return request.user == obj.assignee
        return request.user in obj.contributors.all()
