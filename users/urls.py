from django.urls import path

from users.views import Userlist, user_auth

urlpatterns_users = [
    path('register/', Userlist.as_view(), name='Userlist'), # local item url created
    path('auth/', user_auth, name='user_auth'),
]
