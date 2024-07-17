from rest_framework import serializers

from authentication.models import CustomUser
from issues.serializers import IssueSerializer
from projects.models import Project
from .models import Comment


class CommentPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ["text", "author", "created_time", "issue"]
        fields = ['id', 'description', 'author', 'issue', 'created_time']


    author_id = serializers.IntegerField(write_only=True)
    issue = IssueSerializer(many=False, read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text", "issue", "author", "created_time"]

    # reproduire ceci
    # projet_id = self.context['view'].kwargs.get('project_pk')
    # projet = Project.objects.filter(pk=projet_id).first()
    # # projet_id = self.context['projects_pk']
    # validated_data['project'] = projet
    #
    # assignee_id = validated_data.pop("assignee_id")
    # validated_data["assignee"] = CustomUser.objects.filter(pk=assignee_id).first()
    # validated_data["created_by"] = self.context["request"].user
    # return super().create(validated_data)

    #     # read_only_fields = ["id", "author", "created_time", "issue"]
    # author_id = serializers.IntegerField(write_only=True)
    # issue = IssueSerializer(many=False, read_only=True)
    # print("author_id", author_id)
    # print("issue,", issue)
    #
    def create(self, validated_data):
        author_id = validated_data.pop("author_id")
        validated_data["issue"] = CustomUser.objects.filter(pk=author_id).first()
        validated_data["created_by"] = self.context['request'].user
        return super().create(validated_data)
