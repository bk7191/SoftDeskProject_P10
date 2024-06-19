from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework import permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
# from .serializers import CustomUserSerializer, GroupSerializer
from .permissions import IsAdminAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
    # permission_classes = [IsAdminAuthenticated]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, ]


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model()
    serializer_class = CustomUserSerializer
