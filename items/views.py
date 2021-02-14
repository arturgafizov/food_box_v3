from django.core import cache
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from rest_framework.utils import json

from items.models import Item
from items.models import ItemSerializer
from items.filters import ItemFilter

# Create your views here.
# @api_view(http_method_names=['GET'])
# def item_detail(request, pk):
#     link_item = requests.get('https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json')
#     items = link_item.json()
#     d = {}
#     response = None
#
#     for item in items:
#         if item['id'] == pk:
#             d['id'] = item['id']
#             d['title'] = item['title']
#             d['description'] = item['description']
#             d['image'] = '/media/item_images/' + item['image'].split('/')[-1]
#             d['weight'] = item['weight_grams']
#             d['price'] = item['price']
#             response = d
#
#     if response:
#         return Response(response)
#     elif link_item.status_code == 404:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     elif link_item.status_code == 408:
#         return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


ITEM_CACHE_KEY = 'item_cache_{}'
ITEM_CACHE_TTL = 300


class ItemList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ItemFilter
    search_fields = ['price', 'title']
    ordering = ['price']

    # @method_decorator(cache_page(60 * 5))  # 5 min
    # @method_decorator(vary_on_cookie)
    # def list(self, *args, **kwargs):
    #     return super().list(*args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        key = ITEM_CACHE_KEY.format(request.item.id)
        print(key)
        cached_response = cache.get(key)
        print(cached_response)
        if cached_response:
            print(json.loads(cached_response))
            return Response(json.loads(cached_response), status=status.HTTP_200_OK)
        else:
            response = super().retrieve(request, *args, **kwargs)
            cache.set(key, json.dumps(response.data), ITEM_CACHE_TTL)
            print(response)
            return response

    def get_object(self):
        return self.request.item


class ItemRetrieve(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# @api_view(http_method_names=['GET'])
# def get_item_view(request, pk):
#     item = Item.objects.get(id=pk)
#
#     return Response({
#         'id': item.id,
#         'title': item.title,
#         'description': item.description,
#         'weight': item.weight,
#         'price': item.price,
#     })


