
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

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
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # permission_classes = [IsAuthenticated, IsContributor]

    # def get_queryset(self):
    #     project = get_object_or_404(Project, id=self.kwargs["project_id"])
    #     queryset = Issue.objects.filter(project=project)
    #     return queryset.ordering("created_time")
    #
    # def perform_create(self, serializer):
    #     """
    #     Perform a create on the serializer, ensuring project is included.
    #     """
    #     project = get_object_or_404(Project, pk=self.kwargs["project_pk"])
    #     serializer.save(author=self.request.user, project=project)
    #
    # def get_serializer_class(self):
    #     # à traiter dans permissions
    #     if self.action == 'list':
    #         return ProjectAuthorSimpleSerializer
    #
    #     return self.serializer_class
    #
    # def destroy(self, request, *args, **kwargs):
    #     # à traiter dans permissions qui a droit pour customUser
    #     if self.action == "delete":
    #         issues = Issue.objects.get(pk=issue_pk)
    #         issues.delete()
    def list(self, request, *args, **kwargs):
        """
        Get a list of issues
        """
        issues = self.get_queryset()
        serializer = self.get_serializer(issues, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Get a specific issue
        """
        issue = self.get_object()
        serializer = self.get_serializer(issue)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create a new issue
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Update an issue
        """
        partial = kwargs.pop('partial', False)
        issue = self.get_object()
        serializer = self.get_serializer(issue, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an issue
        """
        issue = self.get_object()
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
