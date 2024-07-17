from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from issues.models import Issue
from issues.serializers import IssueSerializer
from projects.models import Project
from projects.permissions import IsContributor, IsAuthor
from projects.serializers import ProjectAuthorSimpleSerializer


class IssueViewSet(viewsets.ModelViewSet):
    """
    class Issue réservée aux utilisateurs connectes et authentifiés

    """

    # authentication_classes = [JWTAuthentication]

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated & (IsContributor | IsAuthor)]

    http_method_names = ["get", "post", "put", "delete"]

    def get_queryset(self):
        print(self.kwargs)
        project_id = self.kwargs.get('project_pk')
        print("project_id----->", project_id)
        return Issue.objects.filter(project=project_id)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class IssueReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectAuthorSimpleSerializer

    class Meta(IssueViewSet):
        def get_queryset(self):
            return Project.objects.all()
