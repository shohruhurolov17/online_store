from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin


# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin, ]
