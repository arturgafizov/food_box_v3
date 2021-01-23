from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from rest_framework.serializers import ModelSerializer


class User(AbstractUser):
    middle_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
