from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
# from .serializers import CustomUserSerializer, GroupSerializer,
from .permissions import IsAuthenticatedOrReadOnly
from .serializers import CustomUserSerializer, SignupSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
    # permission_classes = [IsAdminAuthenticated]
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, ]


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    # serializer_class = CustomUserCreateSerializer
    serializer_class = SignupSerializer

    # permission_classes = [IsAuthenticatedOrReadOnly]
