from rest_framework import serializers

from authentication.models import CustomUser
from .models import Project, Contributor


class ProjectSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Project.

    Ce sérialiseur permet de convertir les instances du modèle Project en
    représentations JSON et vice-versa. Il utilise la classe ModelSerializer
    de Django REST Framework pour automatiser la création des champs de
    sérialisation à partir des champs du modèle.

    """
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    contributor = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=False)

    def create(self, validated_data):
        author = validated_data.pop("author")
        author_instance = Project.objects.get(pk=author)
        validated_data["contributor"] = author_instance
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project.author
        fields = "__all__"


class ProjectAuthorSimpleSerializer(serializers.ModelSerializer):
    author_obj = ProjectAuthorSerializer(source='author', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        contributor = Contributor.objects.create(project=validated_data['project_id'], user=validated_data['user_id'])

        return contributor

    def get_contributors(self, project):
        contributor = Contributor.objects.filter(project=project)
        return contributor

    def update_contributor(self, contributor, user):
        contributor.user = user
        contributor.save()
        return contributor

    def delete_contributor(self, contributor):
        contributor.delete()


class ContributorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

    def perform_create(self, serializer):
        serializer.save()
