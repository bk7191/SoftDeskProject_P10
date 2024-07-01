from rest_framework import status, viewsets, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import projects
import projects.serializers
from authentication.permissions import *
from projects.models import *
from authentication.serializers import *
from projects.permissions import IsProjectContributorAuthenticated, IsContributor, CanManageProjectContributors
from rest_framework_simplejwt.authentication import JWTAuthentication
from projects.serializers import (
    ProjectSerializer,
    ContributorDetailSerializer,
    ContributorSerializer,
)
from projects.mixins import *


class AdminProjectsViewSet(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()


class ProjectViewSet(viewsets.ModelViewSet, GetDetailSerializerClassMixin, RecordInterestView):
    authentication_classes = [JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # http_method_names = ["get", "post", "head", "patch", "delete"]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Authenticated'})

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        author_queryset = projects.serializers.ContributorSerializer
        return super().update(request, author_queryset, *kwargs)


class ContributorViewSet(viewsets.ModelViewSet, GetDetailSerializerClassMixin):
    authentication_classes = [JWTAuthentication]

    queryset = Contributor.objects.all()

    detail_serializer_class = ContributorDetailSerializer
    serializer_class = ContributorSerializer
    # permission_classes = [IsAuthenticated, IsCreationAndIsStaff]
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # def get_queryset(self):
    #     return Contributor.objects.all()
