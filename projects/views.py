from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from projects.mixins import *
from projects.permissions import IsAuthor
from projects.serializers import *


class ProjectViewSet(ModelViewSet, MultipleSerializerMixin):
    # authentication_classes créée jeton dans authentication.views
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

    queryset = Contributor.objects.all()

    detail_serializer_class = ContributorDetailSerializer
    serializer_class = ContributorSerializer
    # permission_classes = [IsAuthenticated, IsCreationAndIsStaff]
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated & IsAuthor]
