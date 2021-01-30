from django.contrib.auth.models import AbstractUser
from django.db import models
from requests import Response
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.serializers import UniqueTogetherValidator
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


class User(AbstractUser):
    middle_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class UserSerializer(ModelSerializer):
    first_name = models.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'middle_name', 'phone_number', 'address')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('email',)
            )
        ]


class UserCurrentSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'middle_name', 'phone_number', 'address')



