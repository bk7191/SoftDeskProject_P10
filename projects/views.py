from django.contrib.auth import get_user_model
from rest_framework import viewsets

UserModel = get_user_model()


class ProjectViewSet(viewsets.ModelViewSet):


# CRUD projets


class AdminProjectListView(viewsets.ReadOnlyModelViewSet):


class ContributorViewSet(viewsets.ModelViewSet):
