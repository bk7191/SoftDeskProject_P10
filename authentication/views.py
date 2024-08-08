from rest_framework import viewsets, generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from projects.mixins import GetDetailSerializerClassMixin
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserDetailedSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    detail_serializer_class = CustomUserDetailedSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated | IsCreationAndIsStaff | IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["username"]

    @swagger_auto_schema(
        operation_description="This method return the user object (current user)",
        responses={200: CustomUserSerializer},
    )
    def get_serializer_class(self):
        if self.action in ["retrieve", "put", 'get'] and self.permission_classes == 'IsAdminAuthenticated':
            return CustomUserDetailedSerializer
        return CustomUserSerializer


class CustomUserRegisterViewSet(viewsets.ModelViewSet, GetDetailSerializerClassMixin):
    # print(authentication_classes)
    authentication_classes = [JWTAuthentication]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    detail_serializer_class = CustomUserDetailedSerializer
    permissions_classes = [AllowAny]

    filter_backends = [SearchFilter]
    search_fields = [
        "username",
    ]

    def get_serializer_class(self):
        serializer_class = CustomUserSerializer

        if self.action in ["list", 'get', 'retrieve', 'update', 'partial_update', 'destroy']:
            return serializer_class

        return self.detail_serializer_class

    def get(self, request):
        # liste request.users si request.user est enregistré
        user = CustomUser.objects.get(username=request.username)
        user_data = CustomUserSerializer(user).data
        return Response(user_data)


class Home(APIView):
    # authentication_classes = [JWTAuthentication]

    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {"message": "Hello, Bienvenue dans SoftDeskApi!"}
        return Response(content)
