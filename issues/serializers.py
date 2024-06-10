from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    assignee = serializers.IntegerField(read_only=True)
    created_by = serializers.IntegerField(write_only=True, )

    class Meta:
        model = Issue
        fields = "__all__"

