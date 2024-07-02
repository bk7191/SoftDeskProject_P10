from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
# from .serializers import CustomUserSerializer, GroupSerializer,
from .permissions import IsOwnerOrReadOnly, IsAdminAuthenticated, IsCreationAndIsStaff
from .serializers import CustomUserSerializer, CustomUserDetailedSerializer
from rest_framework_simplejwt.tokens import Token


class CustomUserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]

    queryset = CustomUser.objects.all()
    # serializer_class = CustomUserSerializer
    # permission_classes = [IsTheUser, ]
    permission_classes = [IsAuthenticated | IsCreationAndIsStaff | IsOwnerOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["username"]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CustomUserDetailedSerializer
        return CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated | IsCreationAndIsStaff | IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserPrivateSerializer
        return UserPublicSerializer


# class CustomUserDetailViewSet(viewsets.ModelViewSet):
#     authentication_classes = [JWTAuthentication]
#
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
# permission_classes = [IsTheUser, ]
# permission_classes = [IsAuthenticated | IsAdminAuthenticated]
# filter_backends = [SearchFilter]
# search_fields = ["username"]
# permission_classes = [IsAuthenticated, IsOwnerOrReadOnly, IsCreationAndIsStaff]
# permission_classes = [IsAdminAuthenticated]

class CustomUserSignupViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = [
        "username",
    ]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            print(token.key)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalids credentials'}, status=status.HTTP_400_BAD_REQUEST)

class Home(APIView):
    authentication_classes = [JWTAuthentication]

    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {"message": "Hello, World!"}
        return Response(content)
