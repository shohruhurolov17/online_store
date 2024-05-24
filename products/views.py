from rest_framework.decorators import (
    api_view,
    permission_classes,

)
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Product
)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly, IsAdmin
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
# Create your views here.
from .serializers import ProductSerializer


@extend_schema(
    methods=['POST'],
        parameters=[
            OpenApiParameter(
                "product category",
                type={"type": "STR"}, style="form", required=True,
            ),
            OpenApiParameter(
                "product name",
                type={"type": "string"}, style="form", required=True,
            ),
            OpenApiParameter(
                "product desc",
                type={"type": "string"}, style="form", required=True,
            ),
            OpenApiParameter(
                "product price",
                type={"type": "int"}, style="form", required=True,
            ),
            OpenApiParameter(
                "product initial_quantity",
                type={"type": "int"}, style="form", required=True,
            ),
            OpenApiParameter(
                "product image",
                type={"type": "file"}, style="form", required=True,
            )
       ])
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsAdmin, ])
def product_list(request):
    if request.method == 'GET':
        paginator = LimitOffsetPagination()
        paginator.default_limit = 2
        queryset = Product.objects.all()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = ProductSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdmin, ])
def product_detail(request, pk):

    try:
        product = Product.objects.get(id=pk)

    except Product.DoesNotExist:
        return Response({'detail': f'ID si {pk} ga teng mahsulot yo\'q'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response({'detail': f'ID si {pk} ga teng mahsulot o\'chirildi'}, status=status.HTTP_204_NO_CONTENT)