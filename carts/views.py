from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

# Create your views here.
from carts.serializers import CartSerializer, CartItemSerializer
from carts.models import Cart, CartItem
from rest_framework.viewsets import ModelViewSet


class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = permissions.IsAuthenticated
    # lookup_field = 'user_id'
    # lookup_url_kwarg = 'user'

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(cart=user)
        # return super(CartListViewSet, self).get_object()

    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #
    #     if pk == "current":
    #         return self.request.user
    #
    #     return super(CartListViewSet, self).get_object()


class CartItemList(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
