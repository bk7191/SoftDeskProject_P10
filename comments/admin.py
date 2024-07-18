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


admin.site.register(Comment, CommentAdmin)
