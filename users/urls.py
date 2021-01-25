from django.urls import path

from users.views import UserList, UserAuth
from users.views import user_auth

urlpatterns_users = [
    path('register/', UserList.as_view(), name='UserList'), # local item url created
#    path('auth/', UserAuth, name='UserAuth'),
    path('auth/', user_auth, name='user_auth'),
]
