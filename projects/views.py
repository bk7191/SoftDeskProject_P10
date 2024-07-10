from rest_framework import status, viewsets, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

import projects
import projects.serializers
from authentication.permissions import *
from comments.serializers import CommentSerializer
from issues.serializers import IssueSerializer
from projects.models import *
from authentication.serializers import *
from projects.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from projects.serializers import *
from projects.mixins import *


class AdminProjectsViewSet(
    MultipleSerializerMixin, StaffEditorPermissionsMixin, ModelViewSet
):
    serializer_class = ProjectSerializer
    detail_serializer_class = [ProjectDetailSerializer | ContributorDetailSerializer]
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Project.objects.all()


# class ProjectViewSet(ModelViewSet, GetDetailSerializerClassMixin, RecordInterestView):
class ProjectViewSet(ModelViewSet, MultipleSerializerMixin):
    # authentication_classes = [JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    detail_serializer_class = ContributorDetailSerializer
    issue_serializer_class = IssueSerializer
    comments_serializer_class = CommentSerializer
    http_method_names = ["get", "post", "put", "delete"]
    # permission_classes = [IsAuthenticated | IsContributor | IsAuthor]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Authenticated"})

    def put(self, request, *args, **kwargs):
        kwargs["partial"] = True
        author_queryset = projects.serializers.ContributorSerializer
        print(author_queryset)

        return super().update(request, author_queryset, *kwargs)


class ContributorViewSet(viewsets.ModelViewSet, GetDetailSerializerClassMixin):
    # authentication_classes = [JWTAuthentication]

    queryset = Contributor.objects.all()

    detail_serializer_class = ContributorDetailSerializer
    serializer_class = ContributorSerializer
    # permission_classes = [IsAuthenticated, IsCreationAndIsStaff]
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # def get_queryset(self):
    #     return Contributor.objects.all()
