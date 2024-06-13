from rest_framework import serializers

from issues.serializers import IssueSerializer
from .models import Comment


class CommentPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text", "author", "created_time", "issue"]

    author_id = serializers.IntegerField(write_only=True)
    issue = IssueSerializer(many=False, read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    #     # read_only_fields = ["id", "author", "created_time", "issue"]
    # author_id = serializers.IntegerField(write_only=True)
    # issue = IssueSerializer(many=False, read_only=True)
    # print("author_id", author_id)
    # print("issue,", issue)
    #
    # def create(self, validated_data):
    #     author_id = validated_data.pop("author_id")
    #     validated_data["issue"] = CustomUser.objects.filter(pk=author_id).first()
    #     validated_data["created_by"] = self.context['request'].user
    #     return super().create(validated_data)
