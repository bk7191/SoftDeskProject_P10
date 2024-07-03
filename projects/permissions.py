from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import Contributor
from issues.models import Issue


class IsProjectContributorAuthenticated(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    #
    # def has_permission(self, request, view):
    #     if request.user.is_staff:
    #         return True
    #     if request.method == "POST":
    #         project_contributors = [
    #             user.user_id
    #             for user in Contributor.objects.filter(
    #                 project_id=validated_data["project_id"]
    #             )
    #         ]
    #         if request.user.id in project_contributors:
    #             return True
    #         else:
    #             raise PermissionDenied(
    #                 "You must be contributing to this project to do this"
    #             )
    #     return request.user.is_authenticated
    #
    # def has_object_permission(self, request, view, obj):
    #     project_contributors = [
    #         user.user_id for user in Contributor.objects.filter(project_id=obj.id)
    #     ]
    #     if isinstance(obj, Issue):
    #         project_contributors.extend(
    #             user.user_id
    #             for user in Contributor.objects.filter(project_id=obj.project)
    #         )
    #
    #     return request.user.id in project_contributors


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


class IsAuthor(BasePermission):
    # Allow any author to edit,
    # Assumes the model instance has an 'author' attribute.

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
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
