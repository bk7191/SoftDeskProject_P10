from django.conf import settings
from django.db import models
from authentication.models import CustomUser


class Project(models.Model):
    CHOICES = [('back-end', 'back-end'), ('front-end', 'front-end'), ('iOS', 'iOS'), ('android', 'android')]
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=3096, blank=True)
    project_type = models.CharField(max_length=255, choices=CHOICES, verbose_name='Type')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creators')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributeurs')
    contributor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contributor_of')
