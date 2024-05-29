from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from issues.serializers import IssueSerializer
from issues.models import Issue
from projects.models import Project
from projects.serializers import ProjectAuthorSimpleSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilistateurs connectes et authentifiés

    """
    # queryset = User.objects.all()
    serializer_class = IssueSerializer
    # permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "head", "patch", "delete"]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectAuthorSimpleSerializer

        return self.serializer_class
