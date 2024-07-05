from rest_framework import viewsets

from issues.models import Issue
from issues.serializers import IssueSerializer


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
