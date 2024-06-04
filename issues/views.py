from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from comments.permissions import ContributorPermission
from issues.permissions import IsContributor
from issues.serializers import IssueSerializer
from issues.models import Issue
from projects.models import Project
from projects.serializers import ProjectAuthorSimpleSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilisateurs connectes et authentifiés

    """
    # queryset = User.objects.all()
    serializer_class = IssueSerializer
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # permission_classes = [IsAuthenticated, IsContributor]

    def get_queryset(self):
        project = self.kwargs["project_pk"]
        return Issue.objects.filter(project__pk=project_pk)

    def perform_create(self, serializer):
        """
        Perform a create on the serializer, ensuring project is included.
        """
        project = get_object_or_404(Project, pk=self.kwargs["project_pk"])
        serializer.save(author=self.request.user, project=project)

    def get_serializer_class(self):
        # à traiter dans permissions
        if self.action == 'list':
            return ProjectAuthorSimpleSerializer

        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        # à traiter dans permissions qui a droit pour customUser
        if self.action == "delete":
            issues = Issue.objects.get(pk=issue_pk)
            issues.delete()
