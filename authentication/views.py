from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
# from .serializers import CustomUserSerializer, GroupSerializer,
from .permissions import IsTheUser, IsOwnerOrReadOnly
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsTheUser, ]
    permission_classes = [IsAuthenticated | IsOwnerOrReadOnly]

    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
    # permission_classes = [IsAdminAuthenticated]
    def get(self, request, format=None):
        pass
