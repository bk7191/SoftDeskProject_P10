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

    Attributs:
        Meta (classe): Classe de métadonnées pour configurer le sérialiseur.
            model (classe): Le modèle à sérialiser (Project).
            fields (str ou liste): Les champs du modèle à inclure dans la
                sérialisation. '__all__' signifie que tous les champs seront
                inclus.

    Exemple d'utilisation:
        from rest_framework import serializers
        from .models import Project

    """
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    contributors = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=False)

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
        contributor = Contributor.objects.create(project=validated_data['project'], user=validated_data['user'])
        return contributor

    def get_contributors(self, project):
        contributors = Contributor.objects.filter(project=project)
        return contributors

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
