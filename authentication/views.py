from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token
from drf_yasg.utils import swagger_auto_schema
from .models import CustomUser
from .permissions import (
    IsAdminAuthenticated,
    IsCreationAndIsStaff,
    IsOwnerOrReadOnly,
    IsStaffPermission,
)
from .serializers import CustomUserSerializer, CustomUserDetailedSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]

    queryset = CustomUser.objects.all()
    serializer_class = [CustomUserDetailedSerializer]
    permission_classes = [IsCreationAndIsStaff | IsAdminAuthenticated]
    # permission_classes = [IsAuthenticated | IsCreationAndIsStaff | IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["username"]

    @swagger_auto_schema(
        operation_description="This method return the user object (current user)",
        responses={200: CustomUserSerializer},
    )
    def get_serializer_class(self):
        if self.action == "retrieve":
            return CustomUserDetailedSerializer
        return CustomUserSerializer


class CustomUserSignupViewSet(viewsets.ModelViewSet):
    # print(authentication_classes)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailedSerializer
    # permissions_classes = [IsStaffPermission]

    filter_backends = [SearchFilter]
    search_fields = [
        "username",
    ]

    def post(self, request, *args, **kwargs):
        authentication_classes = [JWTAuthentication]

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:

            token, created = authentication_classes.objects.get_or_create(username=user)
            print(token.key)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "Invalids credentials"}, status=status.HTTP_400_BAD_REQUEST
            )

    def list(self, request):
        # liste request.users si request.user est enregistré
        user = CustomUser.objects.get(username=request.user)
        user_data = CustomUserSerializer(user).data
        return Response(user_data)


class Home(APIView):
    authentication_classes = [JWTAuthentication]

    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {"message": "Hello, Bienvenue dans SoftDeskApi!"}
        return Response(content)
