from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "password",
        ]
        read_only_fields = ["created_time"]
        # ajout extra
        extra_kwargs = {"password": {"write_only": True}}


class CustomUserDetailedSerializer(ModelSerializer):
    user = CustomUser.objects.all()

    class Meta(CustomUserSerializer.Meta):
        fields = CustomUserSerializer.Meta.fields + [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "consent_choice",
            "can_be_contacted",
            "can_data_be_shared",
        ]

    def validate_age(self, date_of_birth):
        authorized_age = 16
        age = date_of_birth.age()
        if age < authorized_age:
            raise serializers.ValidationError(f'{authorized_age} requis svp')
        return date_of_birth

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.consent_choice = validated_data.get(
            "consent_choice", instance.consent_choice
        )
        instance.can_be_contacted = validated_data.get(
            "can_be_contacted", instance.can_be_contacted
        )
        instance.can_data_be_shared = validated_data.get(
            "can_data_be_shared", instance.can_data_be_shared
        )
        instance.save()
        return instance
