from django.urls import path
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token
# from users.views import auth_token
# from users.views import sample_api
from users.views import UserList
from users.views import CurrentUserRetrieveUpdateView
# from users.views import UserRegisterViewSet, AuthToken

urlpatterns_users = [
    path('auth/register/', UserList.as_view(), name='UserList'),  # local item url created
    # path('auth/login/', auth_token),
    path('current/', CurrentUserRetrieveUpdateView.as_view(), name='CurrentUser'),
    path('auth/login/', obtain_auth_token)
]
