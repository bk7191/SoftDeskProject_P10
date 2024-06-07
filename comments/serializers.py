from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    issue = serializers.ReadOnlyField(source="project.issue")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "author", "created_time", "issue"]
