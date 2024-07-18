from rest_framework import serializers

from authentication.models import CustomUser
from authentication.serializers import CustomUserSerializer
from .models import Issue, Project


class IssueSerializer(serializers.ModelSerializer):
    assignee_id = serializers.IntegerField(write_only=True)

    assignee = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = Issue
        fields = "__all__"

    def create(self, validated_data):
        projet_id = self.context['view'].kwargs.get('project_pk')
        projet = Project.objects.filter(pk=projet_id).first()
        # projet_id = self.context['projects_pk']
        validated_data['project'] = projet

        assignee_id = validated_data.pop("assignee_id")
        validated_data["assignee"] = CustomUser.objects.filter(pk=assignee_id).first()
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)
