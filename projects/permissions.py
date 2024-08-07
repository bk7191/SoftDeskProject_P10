from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import SAFE_METHODS, BasePermission

from comments.models import Comment
from .models import Contributor, Project
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
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


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

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            project_id = view.kwargs.get("project_pk")
            current_user = request.user
            project = Project.objects.filter(id=project_id).first()
            if project:
                if project.contributeurs.all().filter(user=current_user).count() > 0:
                    return True
                if current_user == project.author:
                    return True
            else:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if isinstance(obj, Project):
            return obj.author == request.user
        elif isinstance(obj, Issue):
            return obj.created_by == request.user
        elif isinstance(obj, Comment):
            return obj.author == request.user
        else:
            return False


class IsContributor(BasePermission):
    #
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            project_id = view.kwargs.get("project_pk")

            current_user = request.user
            project = Project.objects.filter(id=project_id).first()
            print('project contributors+++++++++++++', project.contributeurs.all())
            if project.contributeurs.all().filter(user=current_user).count() > 0:
                return True
            if current_user == project.author:
                return True
        return False
