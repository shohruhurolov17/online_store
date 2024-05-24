from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='products'),
    path('<int:pk>/', product_detail, name='product-detail')
]