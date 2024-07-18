from rest_framework import serializers

from issues.models import Issue
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text", "issue", "author", "created_time"]
        read_only_fields = ["author", "issue"]

    def create(self, validated_data):
        issue_id = self.context['view'].kwargs.get('issue_pk')
        issue = Issue.objects.filter(pk=issue_id).first()
        validated_data["issue"] = issue
        validated_data["author"] = self.context['request'].user
        return super().create(validated_data)
