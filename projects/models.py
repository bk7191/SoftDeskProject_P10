from django.conf import settings
from django.db import models
from authentication.models import CustomUser


class Project(models.Model):
    CHOICES = [
        ("back-end", "back-end"),
        ("front-end", "front-end"),
        ("iOS", "iOS"),
        ("android", "android"),
    ]
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=3096, blank=True)
    project_type = models.CharField(
        max_length=255, choices=CHOICES, verbose_name="Type"
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="creators"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_project_name")
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        if not self.author.filter(pk=self.author.pk).exists():
            self.author.add(self.author)


class Contributor(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="contributeurs"
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="contributor_of"
    )

    class Meta:
        verbose_name = "Contributor"
        verbose_name_plural = "Contributors"
