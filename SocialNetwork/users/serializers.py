from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def validate(self, attrs):
        if attrs.get('password') != attrs.pop('confirm_password'):
            raise serializers.ValidationError({'confirm_password': 'Passwords don\'t match.'})
        return attrs

    def create(self, validated_data):
        get_user_model().objects.create_user(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            password=validated_data.get('password'),
        )
        return validated_data

    def to_representation(self, instance):
        return {'message': 'You have successfully signed up'}


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        update_last_login(None, user)
        return token


class UserActivitySerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    username = serializers.CharField(max_length=100)
    last_login = serializers.DateTimeField()
    last_request = serializers.DateTimeField()
