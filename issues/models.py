from django.db import models
from projects.models import Project, Users


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    priority = models.IntegerField()
    assignee = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='assigned_issues', null=True, blank=True)
    tag = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='created_issues')
    created_time = models.DateTimeField(auto_now_add=True)

