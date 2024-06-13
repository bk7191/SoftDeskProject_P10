from rest_framework import permissions
from rest_framework.permissions import BasePermission

import projects
from .models import Issue
from projects.models import Contributor


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
