from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from authentication.permissions import (
    IsCreationAndIsStaff,
    IsAuthenticatedOrReadOnly,
    ContributorPermission,
)
from comments.models import Comment
from comments.serializers import CommentSerializer
from projects.permissions import IsAuthor


class CommentViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilistateurs connectes et authentifiés

    """

    # authentication_classes = [JWTAuthentication]

    # queryset = Comment.objects.all()
    # serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, IsAuthor]

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
    # comments/views.py

    # class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_pk')
        issue = Issue.objects.get(pk=issue_id)
        serializer.save(author=self.request.user, issue=issue)
