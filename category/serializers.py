from rest_framework import serializers
from .models import Category
from products.models import Product
from products.serializers import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']

    def get_products(self, name):
        products = Product.objects.filter(category=name)
        serializer = ProductSerializer(products, many=True)
        data = [{'id': product['id'], 'name': product['name']} for product in serializer.data]
        return data
