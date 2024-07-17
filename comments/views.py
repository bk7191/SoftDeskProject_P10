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
from issues.models import Issue
from projects.permissions import IsAuthor, IsContributor


class CommentViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilistateurs connectes et authentifiés

    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated & (IsContributor | IsAuthor)]

    def get_queryset(self):
        print(self.kwargs)
        issue_pk = self.kwargs.get('issue_pk')
        print("issues_pk----->", issue_pk)
        return Comment.objects.filter(issue=issue_pk)
