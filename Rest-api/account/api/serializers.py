from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from account.models import CustomUser


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserChangePassword(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)

    def validate(self, attrs):
        errors = []
        new_password = attrs.get("new_password")
        old_password = attrs.get("old_password")
        if new_password == old_password:
            from django.core.exceptions import ValidationError
            raise ValidationError({"new_password": ["bu parola zaten önceki parola"]})

        return attrs

    def validate_new_password(self, value):  # value, gets automatically
        validate_password(value)
        return value


class UserRegister(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "email", "password")


    def validate_password(self, value):
            validate_password(value)
            return value
    def create(self, validated_data):
        username = validated_data.get("username")
        first_name = validated_data.get("first_name")
        email = validated_data.get("email")
        password = validated_data.get("password")

        user = CustomUser.objects.create(username=username, email=email, first_name=first_name)
        user.set_password(password)
        user.save()
        return user


class UserEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "avatar", "email")

