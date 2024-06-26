from rest_framework import status, viewsets, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import projects
import projects.serializers
from authentication.permissions import *
from projects.models import *
from authentication.serializers import *
from projects.permissions import IsProjectContributorAuthenticated, IsContributor
from projects.serializers import (
    ProjectSerializer,
    ContributorDetailSerializer,
    ContributorSerializer,
)
from projects.mixins import *


class ProjectViewSet(viewsets.ModelViewSet, GetDetailSerializerClassMixin):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # http_method_names = ["get", "post", "head", "patch", "delete"]

    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, ContributorPermission]

    def get_view_name(self):
        pass


    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        author_queryset = projects.serializers.ContributorSerializer
        return super().update(request, author_queryset, *kwargs)


class ContributorViewSet(viewsets.ModelViewSet, GetDetailSerializerClassMixin):
    queryset = Contributor.objects.all()

    detail_serializer_class = ContributorDetailSerializer
    serializer_class = ContributorSerializer
    # permission_classes = [IsAuthenticated, IsCreationAndIsStaff]
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # def get_queryset(self):
    #     return Contributor.objects.all()
