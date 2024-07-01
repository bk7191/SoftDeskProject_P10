from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

import issues.serializers
import projects
from authentication.permissions import IsCreationAndIsStaff, IsAuthenticatedOrReadOnly
from comments.permissions import ContributorPermission
from projects.permissions import IsContributor, IsAuthor
from issues.serializers import IssueSerializer
from issues.models import Issue
from projects.models import Project
from projects.serializers import ProjectAuthorSimpleSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilisateurs connectes et authentifiés

    """
    # authentication_classes = [JWTAuthentication]

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    # permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, ]

    # permission_classes = [IsAuthenticated, IsCreationAndIsStaff, IsContributor]
    http_method_names = ["get", "post", "head", "patch", "delete"]

# class IssueViewSet(ReadOnlyModelViewSet):
#     serializer_class = ProjectAuthorSimpleSerializer
#
#     def get_queryset(self):
#         return Project.objects.all()
