from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.permissions import *
from comments.serializers import CommentSerializer
from issues.serializers import IssueSerializer
from projects.mixins import *
from projects.permissions import IsAuthor, IsContributor
from projects.serializers import *


class AdminProjectsViewSet(
    MultipleSerializerMixin, StaffEditorPermissionsMixin, ModelViewSet
):
    serializer_class = ProjectSerializer
    detail_serializer_class = [ProjectDetailSerializer | ContributorDetailSerializer]
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Project.objects.all()


class DisplayProjectMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_issue(self, request, *args, **kwargs):
        instance = self.get_object()
        issue_queryset = instance.issue.all()
        issue_serializer = self.get_issue_serializer(issue_queryset, many=True)
        return Response(issue_serializer.data)

    def get_comment(self, request, *args, **kwargs):
        instance = self.get_object()
        comment_queryset = instance.comment.all()
        comment_serializer = self.get_comment_serializer(comment_queryset, many=True)
        return Response(comment_serializer.data)

    def get_issue_serializer(self, *args, **kwargs):
        return self.serializer_class.issue_serializer_class(*args, **kwargs)

    def get_comment_serializer(self, *args, **kwargs):
        return self.serializer_class.comment_serializer_class(*args, **kwargs)


class ProjectViewSet(ModelViewSet, MultipleSerializerMixin):
    # authentication_classes = [JWTAuthentication]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    detail_serializer_class = ContributorDetailSerializer

    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated & IsAuthor]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ContributorViewSet(viewsets.ModelViewSet, GetDetailSerializerClassMixin):
    # authentication_classes = [JWTAuthentication]

    queryset = Contributor.objects.all()

    detail_serializer_class = ContributorDetailSerializer
    serializer_class = ContributorSerializer
    # permission_classes = [IsAuthenticated, IsCreationAndIsStaff]
    http_method_names = ["get", "post", "head", "patch", "delete"]

    # def get_queryset(self):
    #     return Contributor.objects.all()
