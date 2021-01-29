from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

# Create your views here.
from carts.models import CartSerializer, CartItemSerializer
from carts.models import Cart, CartItem


class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemList(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
