from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from carts.models import Cart, CartItem
from items.models import ItemSerializer


class CartItemSerializer(ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = CartItem
        fields = ('item', 'cart', 'quantity', 'price', 'item_id', 'total_price')
        extra_kwargs = {
            'price': {'read_only': True},
            'total_price': {'read_only': True},
            'quantity': {'required': False},
        }


# class CartSerializer(ModelSerializer):
#     items = CartItemSerializer(many=True, read_only=False)
#
#     class Meta:
#         model = Cart
#         fields = ('id', 'items', 'total_cost')
#         extra_kwargs = {
#             'total_cost': {'read_only': True},
#         }


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=False)
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='carts:user-detail',
    #     lookup_field='user',
    #     format='html'
    # )

    class Meta:
        model = Cart
        fields = ('id', 'total_cost', 'items')
