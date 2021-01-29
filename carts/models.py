from django.db import models
from rest_framework.serializers import ModelSerializer

from users.models import User
from items.models import Item

# Create your models here.


class Cart(models.Model):
    items = models.ManyToManyField(to=Item,  through='CartItem')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cartitems')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=13, decimal_places=2)


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('items', 'user',)


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('item', 'cart', 'quantity', 'price', 'item_id',)
        extra_kwargs = {
            'price': {'read_only': True}
        }
