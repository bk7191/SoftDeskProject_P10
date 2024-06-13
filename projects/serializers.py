from rest_framework import serializers

from authentication.models import CustomUser
from .models import Project, Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"

    def create(self, validated_data):
        print("ContributorSerializer", validated_data)
        contributor = Contributor.objects.create(
            project=validated_data["project"], user=validated_data["user"]
        )

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


class ProjectSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Project.

    Ce sérialiseur permet de convertir les instances du modèle Project en
    représentations JSON et vice-versa. Il utilise la classe ModelSerializer
    de Django REST Framework pour automatiser la création des champs de
    sérialisation à partir des champs du modèle.

    """

    author = serializers.PrimaryKeyRelatedField(read_only=True)
    # contributor = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=True)
    contributeurs = ContributorSerializer(many=True, read_only=True)

    def create(self, validated_data):
        author = self.context["request"].user
        print(author)
        validated_data["author"] = author
        return super().create(validated_data)

    def perform_update(self, serializer):
        serializer.save()

    class Meta:
        model = Project
        fields = [
            "name",
            "contributeurs",
            "description",
            "project_type",
            "author",
            "created_time",
        ]


class ProjectAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project.author
        fields = "__all__"


class ProjectAuthorSimpleSerializer(serializers.ModelSerializer):
    author_obj = ProjectAuthorSerializer(source="author", read_only=True)

    class Meta:
        model = Project
        fields = "__all__"


class ContributorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"

    def perform_create(self, serializer):
        serializer.save()
