from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
# from .serializers import CustomUserSerializer, GroupSerializer,
from .permissions import IsOwnerOrReadOnly, IsAdminAuthenticated, IsCreationAndIsStaff
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsTheUser, ]
    permission_classes = [IsAuthenticated | IsCreationAndIsStaff | IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["username"]
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
    # permission_classes = [IsAdminAuthenticated]


class CustomUserDetailViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsTheUser, ]
    permission_classes = [IsAuthenticated | IsAdminAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["username"]
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
    # permission_classes = [IsAdminAuthenticated]
