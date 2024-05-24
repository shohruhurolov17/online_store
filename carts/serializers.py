from rest_framework import serializers
from .models import (
    Cart
)

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items']

    def get_cart_items(self, id):
        products = CartItem.objects.filter(cart=id)
        serializer = CartItemSerializer(products, many=True)
        data = [{'id': product['id'], 'product': product['product'], 'quantity': product['quantity']} for product in
                serializer.data]
        return data
