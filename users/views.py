import serializer as serializer
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from users.models import User
from users.models import UserSerializer
# from users.models import UserAuthSerializer


class UserList(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

