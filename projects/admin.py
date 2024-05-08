from django.contrib import admin
from authentication.models import CustomUser  # Assuming Users model is in 'authentication' app
from .models import Project, Contributor  # Assuming models are in the same app


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'project_type', 'author',
        'created_time')  # Fields to display in the list view
    search_fields = ('name', 'description', 'project_type')  # Fields to search by
    list_filter = ('project_type',)  # Fields to filter by
    ordering = ('name',)  # Default sorting by project name


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("contributor", 'project')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Contributor, ContributorAdmin)
