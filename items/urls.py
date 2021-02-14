from django.urls import path

from items.views import ItemRetrieve, ItemList

urlpatterns_items = [
    path('<int:pk>/', ItemRetrieve.as_view(), name='item-retrieve'),
    path('', ItemList.as_view(), name='items-list'),
]
