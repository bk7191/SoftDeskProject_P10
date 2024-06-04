from django.contrib.auth.models import User, Group
from rest_framework import serializers

from projects.models import Contributor
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'date_of_birth', 'consent_choice', 'can_be_contacted',
                  'can_data_be_shared', 'created_time']
        read_only_fields = ['created_time']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.consent_choice = validated_data.get('consent_choice', instance.consent_choice)
        instance.can_be_contacted = validated_data.get('can_be_contacted', instance.can_be_contacted)
        instance.can_data_be_shared = validated_data.get('can_data_be_shared', instance.can_data_be_shared)
        instance.save()
        return instance


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'is_staff']

    def create(self, validated_data):
        users = User(
            username=validated_data["username"],
            can_be_contacted=validated_data["can_be_contacted"],
            can_data_be_shared=validated_data["can_data_be_shared"],
        )
        users.set_password(validated_data["password"])
        users.save()
        return users

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.can_be_contacted = validated_data.get("can_be_contacted", instance.can_be_contacted)
        instance.can_data_be_shared = validated_data.get("can_data_be_shared", instance.can_data_be_shared)
        instance.age = validated_data.get("age", instance.age)
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
        instance.save()
        return instance


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'

    def create(self, project):
        contributor = Contributor.objects.create(project=project)
        return contributor

    def get_contributors(self, project):
        contributors = Contributor.objects.filter(project=project)
        return contributors

    def update_contributor(self, contributor, user):
        contributor.contributor = user
        contributor.save()
        return contributor

    def delete_contributor(self, contributor):
        contributor.delete()


class ContributorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
