from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.permissions import IsOwnerOrReadOnly
from projects.models import *
from authentication.serializers import *
from projects.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer(queryset, many=True)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # 1. List all
    def get_project(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        return Response(serializer_class.data, status=status.HTTP_200_OK)

    # 2. Create
    def post_project(self, request, *args, **kwargs):
        '''
        Create the Project with given projects data
        '''
        data = {
            'task': request.data.get('name'),
            'choice': request.data.get('CHOICES'),
            'completed': request.data.get('completed'),
            'project_type': request.data.get('project_type'),
            'author': request.data.get('author'),
            'created_time': request.data.get('created_time'),
            'user': request.user.id
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContributorViewSet(viewsets.ModelViewSet):
    detail_serializer_class = ContributorDetailSerializer
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Contributor.objects.all()
