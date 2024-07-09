from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet

from issues.models import Issue
from issues.serializers import IssueSerializer
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


class IssueReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = ProjectAuthorSimpleSerializer

    class Meta(IssueViewSet):
        def get_queryset(self):
            return Project.objects.all()
