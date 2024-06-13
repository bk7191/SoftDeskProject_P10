from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

import issues.serializers
import projects
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
