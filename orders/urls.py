from django.urls import path
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


from .views import (
    order_list,
    order_detail,
    OrderItemViewSet,
    order_received
)

urlpatterns = [
    path('orders/', order_list, name='orders'),
    path('order_received/<int:order_id>/', order_received, name='order_received'),
    path('orders/<int:order_id>/', order_detail, name='order-detail'),
]

router.register(r'order-item', OrderItemViewSet, basename='order-item')

urlpatterns += router.urls
