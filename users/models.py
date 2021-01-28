from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers
from rest_framework.serializers import UniqueTogetherValidator
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer


class User(AbstractUser):
    middle_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class UserSerializer(ModelSerializer):
    first_name = models.CharField(max_length=200)

    class Meta:
        model = User
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('email',)
            )
        ]


# class UserAuthSerializer(ModelSerializer):
#     first_name = models.CharField(max_length=200)
#
#     class Meta:
#         model = User
#         fields = ('email', 'password')
