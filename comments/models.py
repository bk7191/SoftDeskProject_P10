from django.db import models
from authentication.models import Users
from issues.models import Issue
import uuid


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
    #     # Métadonnées
    class Meta:
        db_table = "comment"
        ordering = ["created_time"]
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
