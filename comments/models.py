from django.db import models
from authentication.models import CustomUser
from issues.models import Issue
import uuid


class Comment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='auteurs')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
