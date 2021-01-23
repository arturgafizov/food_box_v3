from rest_framework.routers import DefaultRouter

from items.views import Itemlist, Itemretrieve
from django.urls import path
#router = DefaultRouter()
#router.register('items', ItemViewset, basename='item')
#urlpatterns_item = router.urls


urlpatterns_items = [
    path('items/', Itemlist.as_view(), name='Itemlist'),
    path('items/<int:pk>/', Itemretrieve.as_view(), name='Itemretrieve'),
]

