from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from orders.models import Order
from carts.serializers import CartSerializer


class OrderSerializer(ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = ('id', 'cart', 'status', 'total_cost', 'address', 'delivery_at', 'created_at')
        extra_kwargs = {
            'cart': {'read_only': True},
            'status': {'read_only': True},
            'total_cost': {'read_only': True},
            'created_at': {'read_only': True},
        }

    # def validate_address(self, value):
    #     if self.instance and value != self.instance.address:
    #         raise serializers.ValidationError('Something wrong with this field')
    #     return value
