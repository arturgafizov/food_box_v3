from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import requests
from django.core.management.base import BaseCommand
from rest_framework import status, response
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        link_user = requests.get(
            'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json')
        users = link_user.json()
        # print(users)

        for user in users:
            recipient = User.objects.filter(id=user['id']).first()
            # token = Token.objects.create(user=user['username'])
            # print(token.key)
            try:
                d = {'password': make_password(user['password']),
                     'username': user['email'].split('@')[0],
                     'last_name': user['info']['surname'],
                     'first_name': user['info']['name'],
                     'middle_name': user['info']['patronymic'],
                     'email': user['email'],
                     'address': user['city_kladr'],
                     'phone_number': user['contacts']['phoneNumber']}

                new_user = User.objects.update_or_create(defaults=d, id=user['id'])
                self.stdout.write("User successfully created_or_update")
            except ValidationError:
                print("Validation Error")

        if link_user.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif link_user.status_code == 408:
            return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
