from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    issue_id = serializers.ReadOnlyField(source="issue.id")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "author", "created_time", "issue_id"]
