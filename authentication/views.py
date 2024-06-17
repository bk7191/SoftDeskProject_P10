from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer

# from .serializers import CustomUserSerializer, GroupSerializer
from .permissions import IsOwnerOrReadOnly, IsCreationAndIsStaff


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
    permission_classes = [IsAuthenticated, IsCreationAndIsStaff]

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#
#     # permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)
