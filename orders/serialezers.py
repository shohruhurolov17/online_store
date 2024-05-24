from rest_framework import serializers
from .models import (
    Order,
    OrderItem
)
from products.models import Product
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField('get_product')

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity']

    def get_product(self, name):
        product = Product.objects.get(name=name)
        serializer = ProductSerializer(product)
        return serializer.data['name']


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField('get_order_items')

    class Meta:
        model = Order
        fields = ['id', 'user', 'address', 'status', 'order_items']

    def get_order_items(self, order):
        products = OrderItem.objects.filter(order=order)
        serializer = OrderItemSerializer(products, many=True)

        return serializer.data
