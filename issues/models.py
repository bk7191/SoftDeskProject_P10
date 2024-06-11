from django.db import models
from projects.models import Project
from authentication.models import CustomUser


class Issue(models.Model):
    STATUS = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Finished', 'Finished'),
    ]
    PRIORITY = [
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    ]
    TAG = [
        ('BUG', 'BUG'),
        ('FEATURE', 'FEATURE'),
        ('TASK', 'TASK'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS, verbose_name='status')
    priority = models.CharField(max_length=255, choices=PRIORITY, verbose_name='Priority')
    assignee = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='assigned_issues',
                                 limit_choices_to={
                                     'contributor__project': models.F('project')},
                                 blank=True)
    tag = models.CharField(max_length=255, choices=TAG, verbose_name='tag', default="To Do")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_issues')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project} - {self.assignee}'
