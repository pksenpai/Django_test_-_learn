from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(
        max_length=100,
        write_only=True,
    )
    password2 = serializers.CharField(
        write_only=True,
    )
    
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError({
                "password": "Passwords must match!"
            })
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(
        max_length=100,
        write_only=True,
    )
    
    