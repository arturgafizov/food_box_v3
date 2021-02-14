from django.shortcuts import render
from requests import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView

from orders.models import Order
from orders.serializers import OrderSerializer, OrderUpdateSerializer


class OrderLimitOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 6


class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderLimitOffsetPagination
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(recipient=user)


class OrderRetrieve(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderUpdateSerializer
    authentication_classes = (TokenAuthentication, )
