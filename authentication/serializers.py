from datetime import date

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CustomUser, calculer_age
from rest_framework.authtoken.models import Token


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]
        read_only_fields = ["created_time"]
        # ajout extra
        extra_kwargs = {"password": {"write_only": True}}

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {

            'username': representation['username'],
        }


class CustomUserDetailedSerializer(ModelSerializer):
    user = CustomUser.objects.all()

    class Meta(CustomUserSerializer.Meta):
        fields = CustomUserSerializer.Meta.fields + [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "consent_choice",
            "can_be_contacted",
            "can_data_be_shared",
        ]
        read_only_fields = ["age"]

    def validate_date_of_birth(self, date_of_birth):
        authorized_age = 16
        age = calculer_age(date_of_birth)

        if age < authorized_age:
            raise serializers.ValidationError(f'{authorized_age} ans requis svp')
        return date_of_birth

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
