from django.contrib import admin

from .models import CustomUser  # Assuming your model is in the same app


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "can_be_contacted",
        "can_data_be_shared",
        "created_time",
        "is_superuser",
        "is_active",
        "is_staff",
    ]  # Fields to display in the list view
    search_fields = ["username", "email"]  # Fields to search by
    list_filter = [
        "can_be_contacted",
        "can_data_be_shared",
        "groups",
    ]  # Fields to filter by
    ordering = [
        "username",
    ]  # Default sorting by username

    # Don't show the password field
    readonly_fields = [
        "password",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
