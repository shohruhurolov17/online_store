from .views import (
    cart_list,
    cart_detail,
    cart_items_list,
    cart_item_detail
)
from django.urls.conf import path


urlpatterns = [
    path('carts/', cart_list),
    path('carts/<int:pk>/', cart_detail),
    path('cart-items/', cart_items_list),
    path('cart-items/<int:pk>/', cart_item_detail)
]