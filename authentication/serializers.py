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


# desactiver group
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
