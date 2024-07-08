from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import date


# Creation AbstractUser.


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="users")
    user_permissions = models.ManyToManyField(Permission, related_name="users")
    username = models.CharField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    # Attributs RGPD
    age = models.CharField(max_length=2, blank=False, default=False)
    consent_choice = models.BooleanField(default=False)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    # updated_time pour information update
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
