from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.IntegerField()
    issue = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = "__all__"
