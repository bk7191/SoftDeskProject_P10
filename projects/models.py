from django.db import models
from authentication.models import Users


class Project(models.Model):
    # name = models.CharField(max_length=255)
    # description = models.TextField()
    # project_type = models.CharField(max_length=255)
    # contributors = models.ManyToManyField(Users, related_name='contributed_projects', blank=True)
    # created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='created_projects')
    #
    # #     # Métadonnées
    # class Meta:
    #     db_table = "project"
    #     ordering = ["name"]
    #     verbose_name = "Projet"
    #     verbose_name_plural = "Projets"
    pass


class Contributor(models.Model):
    # user = models.ForeignKey(Users, on_delete=models.CASCADE)
    # projects = models.ManyToManyField('project.Project')
    #
    # # Métadonnées
    # class Meta:
    #     db_table = "contributor"
    #     ordering = ["user"]
    #     verbose_name = "Contributeur"
    #     verbose_name_plural = "Contributeurs"
    pass
