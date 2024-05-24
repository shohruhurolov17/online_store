from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.viewsets import ModelViewSet
from .models import (
    Order,
    OrderItem
)
from .serialezers import (
    OrderSerializer,
    OrderItemSerializer
)
from carts.models import Cart, CartItem
from products.models import Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.


@extend_schema(
    methods=['POST'],
    parameters=[
        OpenApiParameter(
            "status",
            type={"type": "str"}, style="form", required=True,
        ),
        OpenApiParameter(
            "user id",
            type={"type": "int"}, style="form", required=True,
        ),
        OpenApiParameter(
            "address",
            type={"type": "str"}, style="form", required=True,
        )
    ])
@api_view(['POST', 'GET'])
def order_list(request):

    if request.method == 'POST':
        user_id = request.data['user']
        try:
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return Response({'detail': 'user mavjud emas'}, status=status.HTTP_404_NOT_FOUND)
        try:
            cart = Cart.objects.get(user=user)

        except Cart.DoesNotExist:
            return Response({'detail': 'userning savatchasi mavjud emas'}, status=status.HTTP_404_NOT_FOUND)

        cart_items = CartItem.objects.filter(cart=cart)

        if cart_items.exists():
            order = Order.objects.create(
                user=user,
                status='pending'
            )

            for item in cart_items:
                product = Product.objects.get(name=item.product)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item.quantity
                )

            cart.delete()
            cart_items.delete()

            return Response({'message': 'Buyurtma muvaffiqiyatli yaratildi'}, status=status.HTTP_201_CREATED)

        else:
            return Response({'error': 'Savatchada mahsulot mavjud emas'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def order_detail(request, order_id):

    try:
        order = Order.objects.get(id=order_id)

    except Order.DoesNotExist:
        return Response({'detail': 'Buyurtma topilmadi'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = OrderSerializer(order, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def order_received(request, order_id):

    try:
        order = Order.objects.get(id=order_id)

    except Order.DoesNotExist:
        return Response({'detail': 'Bunday buyurtma yo\'q'}, status=status.HTTP_404_NOT_FOUND)

    if order.status == 'pending':
        order.status = 'accepted'
        order.save()
        return Response({'detail': 'Buyurtma mijozga yetkazildi'}, status=status.HTTP_200_OK)

    return Response({'detail': 'Buyurtma allaqachon yetkazilgan yoki bekor qilingan'})


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



