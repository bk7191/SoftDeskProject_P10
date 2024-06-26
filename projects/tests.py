import unittest
from django.conf import settings
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import CustomUser
from authentication.views import CustomUserViewSet
from authentication.serializers import CustomUserSerializer


class TestCustomUserViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass"
        )
        self.url = "/api/users/"

    def test_list_custom_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["username"], self.user.username)

    def test_create_custom_user(self):
        data = {"username": "newuser", "password": "newpass"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = CustomUser.objects.get(username="newuser")
        self.assertEqual(user.username, data["username"])

    def test_retrieve_custom_user(self):
        response = self.client.get(f"{self.url}{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_update_custom_user(self):
        data = {"username": "updateduser"}
        response = self.client.patch(f"{self.url}{self.user.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = CustomUser.objects.get(id=self.user.id)
        self.assertEqual(user.username, data["username"])

    def test_delete_custom_user(self):
        response = self.client.delete(f"{self.url}{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(id=self.user.id)


class ProjectTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project_data = {
            "title": "Test Project",
            "description": "This is a test project",
            "github_link": "https://github.com/test-user/test-project",
            "image_link": "https://example.com/test-project-image.jpg",
            "demo_link": "https://example.com/test-project-demo",
            "categories": ["category1", "category2"],
            "owner": "test-user",
        }
        self.create_project()

    def create_project(self):
        response = self.client.post(reverse("project-list"), self.project_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_projects(self):
        response = self.client.get(reverse("project-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project(self):
        response = self.client.get(reverse("project-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        new_project_data = {
            "title": "New Test Project",
            "description": "This is a new test project",
            "github_link": "https://github.com/test-user/new-test-project",
            "image_link": "https://example.com/new-test-project-image.jpg",
            "demo_link": "https://example.com/new-test-project-demo",
            "categories": ["category1", "category2"],
            "owner": "test-user",
        }
        response = self.client.post(reverse("project-list"), new_project_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_project(self):
        new_title = "Updated Test Project"
        new_description = "This is an updated test project"
        response = self.client.patch(
            reverse("project-detail", kwargs={"pk": 1}),
            {"title": new_title, "description": new_description},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], new_title)
        self.assertEqual(response.data["description"], new_description)

    def test_delete_project(self):
        response = self.client.delete(reverse("project-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
