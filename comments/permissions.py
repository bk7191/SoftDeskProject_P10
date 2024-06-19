from rest_framework import permissions


class ContributorPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.issue.project.contributor.all()
