from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import date


# Creation AbstractUser.

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='users')
    user_permissions = models.ManyToManyField(Permission, related_name='users')
    username = models.CharField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    # Attributs RGPD
    date_of_birth = models.DateField(null=True, blank=True)
    consent_choice = models.BooleanField(default=False)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    # updated_time pour information update
    updated_time = models.DateTimeField(auto_now=True)

    @property
    def age(self):
        if not self.date_of_birth:
            return None
        today = date.today()
        return (today.year - self.date_of_birth.year
                - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)))
