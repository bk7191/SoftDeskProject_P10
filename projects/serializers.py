from rest_framework import serializers
from .models import Project


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

        project = Project.objects.get(pk=1)
        serializer = ProjectSerializer(project)
        json_data = serializer.data
    """

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
