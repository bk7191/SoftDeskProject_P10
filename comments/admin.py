from django.contrib import admin

from .models import Comment  # Assuming your model is in the same app


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "author",
        "issue",
        "created_time",
    )  # Fields to display in the list view
    search_fields = ("text",)  # Fields to search by
    list_filter = (
        "issue__project",
    )  # Filter by project (assuming Issue has a foreign key to Project)
    ordering = ("-created_time",)  # Default sorting by most recent creation time

    def has_delete_permission(self, request, obj=None):
        # You can customize deletion permission logic here if needed
        # For example, only allow deleting comments by the author or admins
        return True  # Allow deletion by default


admin.site.register(Comment, CommentAdmin)
