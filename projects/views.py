from django.contrib.auth import get_user_model
from rest_framework import viewsets
from authentication.models import *
from projects.models import *
from authentication.serializers import *
UserModel = get_user_model()


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# CRUD projets


class AdminProjectListView(viewsets.ReadOnlyModelViewSet):


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.project.all()
    serializer_class = CustomUserSerializer
