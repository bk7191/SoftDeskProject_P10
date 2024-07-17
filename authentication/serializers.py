from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CustomUser
from rest_framework.authtoken.models import Token


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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'username': representation['username'],
        }


class CustomUserDetailedSerializer(ModelSerializer):
    user = CustomUser.objects.all()

    class Meta(CustomUserSerializer.Meta):
        fields = CustomUserSerializer.Meta.fields + [
            "first_name",
            "last_name",
            "email",
            "age",
            "consent_choice",
            "can_be_contacted",
            "can_data_be_shared",
        ]

    def validate_age(self, age):
        authorized_age = 16
        if int(age) < authorized_age:
            raise serializers.ValidationError(f'{authorized_age} ans requis svp')
        return age

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        print("user de serializer", user)

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
