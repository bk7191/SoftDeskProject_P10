from rest_framework import viewsets

from .models import CustomUser
# from .serializers import CustomUserSerializer, GroupSerializer
from .permissions import IsAdminAuthenticated
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
    permission_classes = [IsAdminAuthenticated]
