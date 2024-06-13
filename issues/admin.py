from django.contrib import admin
from issues.models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "get_assignee",
        "project",
        "created_by",
        "created_time",
    )  # Fields to display in the list view
    search_fields = ("title", "description", "tag")  # Fields to search by
    list_filter = ("status", "priority", "project")  # Fields to filter by
    ordering = ("-created_time",)  # Default sorting by most recent creation time

    def get_assignee(self, obj):
        return (
            obj.assignee.username if obj.assignee else "-"
        )  # Custom method to display assignee username or '-'

    get_assignee.short_description = (
        "Assigné"  # Label for the custom method in the list view
    )


admin.site.register(Issue, IssueAdmin)
