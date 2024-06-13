from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import projects
from authentication.permissions import IsOwnerOrReadOnly
from projects.models import *
from authentication.serializers import *
from projects.serializers import (
    ProjectSerializer,
    ProjectAuthorSimpleSerializer,
    ContributorDetailSerializer,
    ContributorSerializer,
)
from projects.mixins import *


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()

    detail_serializer_class = ContributorDetailSerializer
    serializer_class = ContributorSerializer
    # permission_classes = [IsAuthenticated, ]
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # def get_queryset(self):
    #     return Contributor.objects.all()
