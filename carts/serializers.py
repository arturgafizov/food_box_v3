from rest_framework.serializers import ModelSerializer

from carts.models import Cart, CartItem
from items.models import ItemSerializer


class CartItemSerializer(ModelSerializer):
    # total_price = serializers.SerializerMethodField()
    item = ItemSerializer()
    # def get_total_price(self, cart_item_instance):
    #     return cart_item_instance.a + cart_item_instance.b

    class Meta:
        model = CartItem
        fields = ('item', 'cart', 'quantity', 'price', 'item_id', 'total_price')
        extra_kwargs = {
            'price': {'read_only': True},
            'total_price': {'read_only': True},
        }


class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=False)


    class Meta:
        model = Cart
        fields = ('id', 'items', 'total_cost')
        extra_kwargs = {
            'total_cost': {'read_only': True},
        }
