from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin

# Register your models here.
from .models import (
    Order,
    OrderItem
)


class OrderItemInlines(TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(ModelAdmin):
    model = Order
    inlines = [OrderItemInlines]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
