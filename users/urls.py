from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserList
from users.views import UserRegisterViewSet

urlpatterns_users = [
    path('auth/register/', UserList.as_view(), name='UserList'),  # local item url created
    path('auth/login/', obtain_auth_token),
]
