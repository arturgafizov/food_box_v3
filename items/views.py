from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from items.models import Item
from items.models import ItemSerializer
from items.filters import ItemFilter

# Create your views here.
@api_view(http_method_names=['GET'])
def item_detail(request, pk):
    link_item = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')
    items = link_item.json()
    d = {}
    response = None

    for item in items:
        if item['id'] == pk:
            d['id'] = item['id']
            d['title'] = item['title']
            d['description'] = item['description']
            d['image'] = '/media/item_images/' + item['image'].split('/')[-1]
            d['weight'] = item['weight_grams']
            d['price'] = item['price']
            response = d

    if response:
        return Response(response)
    elif link_item.status_code == 404:
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif link_item.status_code == 408:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ItemFilter
    search_fields = ['price', 'title']
    ordering = ['price']


class ItemRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
