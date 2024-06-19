from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authentication.permissions import IsCreationAndIsStaff
from comments.models import Comment
from comments.permissions import ContributorPermission
from comments.serializers import CommentSerializer
from issues.permissions import IsAuthor
from issues.views import IssueViewSet


class CommentViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilistateurs connectes et authentifiés

    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # http_method_names = ["get", "put", "patch", "delete"]
    # permission_classes = [IsAuthenticated, IsCreationAndIsStaff, ContributorPermission]

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         permission_classes = [IsAuthenticated, ContributorPermission]
    #     elif self.request.method in ["PUT", "PATCH", "DELETE"]:
    #         permission_classes = [IsAuthenticated, IsAuthor]
    #     return [permission() for permission in permission_classes]

    # def get_queryset(self):
    #     project_pk = self.kwargs["author_id"]
    #     issue_pk = self.kwargs["issue_id"]
    #     uuid = self.kwargs["id"]
    #     return Comment.objects.filter(
    #         issue__project__id=project_pk, issue_id=issue_pk, id=uuid
    #     )
