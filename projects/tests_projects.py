# import unittest

import pytest
import pytest_drf
from django.test import TestCase
from django.urls import reverse
from pytest_drf import APIViewTest, Returns200, UsesGetMethod
from config_API import *
# from rest_framework.test import APIClient
# from rest_framework import status
from projects.models import Project


class TestHelloWorld(
    APIViewTest,
    UsesGetMethod,
    Returns200,
):
    @pytest.fixture
    def url(self):
        return reverse("")

    def test_it_returns_hello_world(self, json):
        expected = "Hello, World!"
        actual = json
        assert expected == actual


def test_return_hello(client):
    response = client.get('')
    data = response.data.decode()
    assert data == "Hello, Bienvenue dans SoftDeskApi!"


class AdminProjectsViewSet(
    MultipleSerializerMixin, StaffEditorPermissionsMixin, ModelViewSet
):
    serializer_class = ProjectSerializer
    detail_serializer_class = [ProjectDetailSerializer | ContributorDetailSerializer]
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return Project.objects.all()


class DisplayProjectMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_issue(self, request, *args, **kwargs):
        instance = self.get_object()
        issue_queryset = instance.issue.all()
        issue_serializer = self.get_issue_serializer(issue_queryset, many=True)
        return Response(issue_serializer.data)

    def get_comment(self, request, *args, **kwargs):
        instance = self.get_object()
        comment_queryset = instance.comment.all()
        comment_serializer = self.get_comment_serializer(comment_queryset, many=True)
        return Response(comment_serializer.data)

    def get_issue_serializer(self, *args, **kwargs):
        return self.serializer_class.issue_serializer_class(*args, **kwargs)

    def get_comment_serializer(self, *args, **kwargs):
        return self.serializer_class.comment_serializer_class(*args, **kwargs)
# from authentication.views import CustomUserViewSet
# from authentication.serializers import CustomUserSerializer
#
# class TestProjects(TestCase):
#     CHOICE_PROJECT = "back-end"
#
#     def setUp(self):
#         self.project_List = Project()
#         self.project_List.name = "Projet 1"
#         self.project_List.description = "desc. proj. 1"
#         self.project_List.project_type = self.CHOICE_PROJECT
#         self.project_List.author = "1"
#
#     def test_create_project(self):
#         nbr_of_projects_before_add = Project.objects.count()
#         print(nbr_of_projects_before_add)
#         nbr_of_projects_after_add = Project.objects.count()
#         print(nbr_of_projects_after_add)

#
# class TestCustomUserViewSet(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = CustomUser.objects.create_user(
#             username="testuser", password="testpass"
#         )
#         self.url = "/api/users/"
#
#     def test_list_custom_users(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]["username"], self.user.username)
#
#     def test_create_custom_user(self):
#         data = {"username": "newuser", "password": "newpass"}
#         response = self.client.post(self.url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         user = CustomUser.objects.get(username="newuser")
#         self.assertEqual(user.username, data["username"])
#
#     def test_retrieve_custom_user(self):
#         response = self.client.get(f"{self.url}{self.user.id}/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["username"], self.user.username)
#
#     def test_update_custom_user(self):
#         data = {"username": "updateduser"}
#         response = self.client.patch(f"{self.url}{self.user.id}/", data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         user = CustomUser.objects.get(id=self.user.id)
#         self.assertEqual(user.username, data["username"])
#
#     def test_delete_custom_user(self):
#         response = self.client.delete(f"{self.url}{self.user.id}/")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         with self.assertRaises(CustomUser.DoesNotExist):
#             CustomUser.objects.get(id=self.user.id)
#
#
# class ProjectTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.project_data = {
#             "name": "est Project",
#             "description": "This is a new test project",
#             # "project_type": "https://github.com/test-user/new-test-project",
#             # "image_link": "https://example.com/new-test-project-image.jpg",
#             # "demo_link": "https://example.com/new-test-project-demo",
#             "project_type": "front-end",
#             "author": "test-user",
#         }
#         self.create_project()
#
#     def create_project(self):
#         response = self.client.post(reverse("projects"), self.project_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_get_projects(self):
#         response = self.client.get(reverse("projects"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_project(self):
#         response = self.client.get(reverse("projects", kwargs={"pk": 1}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_create_project(self):
#         new_project_data = {
#             "name": "New Test Project",
#             "description": "This is a new test project",
#             # "project_type": "https://github.com/test-user/new-test-project",
#             # "image_link": "https://example.com/new-test-project-image.jpg",
#             # "demo_link": "https://example.com/new-test-project-demo",
#             "project_type": "back-end",
#             "author": "test-user",
#         }
#         response = self.client.post(reverse("project-list"), new_project_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_update_project(self):
#         new_title = "Updated Test Project"
#         new_description = "This is an updated test project"
#         response = self.client.patch(
#             reverse("project-detail", kwargs={"pk": 1}),
#             {"title": new_title, "description": new_description},
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["title"], new_title)
#         self.assertEqual(response.data["description"], new_description)
#
#     def test_delete_project(self):
#         response = self.client.delete(reverse("project-detail", kwargs={"pk": 1}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
