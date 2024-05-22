from rest_framework.permissions import IsAuthenticated

from authentication.permissions import IsOwnerOrReadOnly
from projects.models import *
from authentication.serializers import *


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # Create


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.project.all()
    serializer_class = CustomUserSerializer()
    permission_classes = [IsAuthenticated, ]
