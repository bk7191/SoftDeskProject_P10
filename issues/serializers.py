from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    assignee = serializers.IntegerField(read_only=True)
    created_by = serializers.IntegerField(write_only=True, )

    class Meta:
        model = Issue
        fields = "__all__"

    # def create(self, validated_data):
    #     author = validated_data.pop("assignee")
    #     author_instance = Project.objects.get(pk=author)
    #     validated_data["created_by"] = author_instance
    #     return super().create(validated_data)
