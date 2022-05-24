from rest_framework import serializers
from product.models import CustomUser, Product
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=CustomUser.objects.all(),
            message='EMAIL ALREADY EXIST',
        )]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'id', 'email', 'phone_no', 'profile_pic']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "password didn't match"})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'], validated_data['password'], validated_data['email']
        )
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()

        return user

