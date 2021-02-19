import token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
import serializer as serializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import status
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view, permission_classes
import requests
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authentication import TokenAuthentication

from users.models import User
from users.models import UserSerializer, UserCurrentSerializer


# from users.models import AuthTokenSerializer


class UserList(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


class UserRegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
# @ csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def auth_token(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key}, status=HTTP_200_OK)


# получить доступ к API с помощью токена.
# @ csrf_exempt
# @api_view(["GET"])
# def sample_api(request):
#     data = {'sample_data': 123}
#     return Response(data, status=HTTP_200_OK)


class CurrentUserRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserCurrentSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# @api_view(http_method_names=['POST'])
# def user_auth(self, request):
#     data = self.UserAuthSerializer.data
#
#     if request.user.is_authenticated:
#         serializer = UserAuthSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
