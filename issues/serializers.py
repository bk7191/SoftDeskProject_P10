from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    assignee = serializers.IntegerField()
    created_by = serializers.IntegerField()

    class Meta:
        model = Issue
        fields = "__all__"
