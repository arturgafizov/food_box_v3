from django.urls import path

from users.views import user_list

urlpatterns_users = [
    path('register/', user_list, name='item_list'), # local item url created
]
