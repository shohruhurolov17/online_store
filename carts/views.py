from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .models import CartItem, Cart
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer, CartSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

@extend_schema(
    methods=['POST'],
    parameters=[
        OpenApiParameter(
            "user id",
            type={"type": "int"}, style="form", required=True,
        )
    ])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ])
def cart_list(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(id=pk)

    except Cart.DoesNotExist:

        return Response({'detail': f'ID si {pk} ga teng bo\'lgan cart yo\'q'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(cart)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        cart.delete()

        return Response({'detail': f'ID si {pk} ga teng bo\'lgan cart o\'chirildi'}, status=status.HTTP_204_NO_CONTENT)


def add_initial_quantity(pk, quantity):
    product = Product.objects.get(id=pk)
    product.initial_quantity += quantity
    product.save()



@extend_schema(
    methods=['POST'],
    parameters=[
        OpenApiParameter(name='card id', required=True, type=int),
        OpenApiParameter(
            "product name",
            type={"type": "string"}, style="form", required=True,
        ),
        OpenApiParameter(
            "product quantity",
            type={"type": "int"}, style="form", required=True,
        ),

    ]
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ])
def cart_items_list(request):
    if request.method == 'GET':
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']
            product = Product.objects.get(name=product_id)

            if product.initial_quantity >= quantity:
                product.initial_quantity -= quantity
                product.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({
                                    'detail': f'Ogohlantirish, do\'konda {product.name}ning qolgan miqdori {product.initial_quantity} ga teng'})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, ])
def cart_item_detail(request, pk):
    try:
        cart_item = CartItem.objects.get(id=pk)

    except CartItem.DoesNotExist:
        return Response({'detail': f'ID si {pk} ga teng bo\'lgan cart_item yo\'q'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':

        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = CartItemSerializer(cart_item)
        add_initial_quantity(serializer.data['product'], serializer.data['quantity'])
        cart_item.delete()
        return Response({'detail': f'ID si {pk} ga teng bo\'lgan cart_item o\'chirildi'},
                        status=status.HTTP_204_NO_CONTENT)
