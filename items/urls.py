from items.views import Itemretrieve
from django.urls import path

urlpatterns_items = [
    path('<int:pk>/', Itemretrieve.as_view(), name='Itemretrieve'),

]
