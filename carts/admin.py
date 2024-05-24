from django.contrib import admin
from django.contrib.admin import TabularInline, ModelAdmin
# Register your models here.
from .models import Cart, CartItem


class CartItemInlines(TabularInline):
    model = CartItem
    extra = 0


class CartItemAdmin(ModelAdmin):
    model = CartItem
    list_display = ['id', 'cart', 'product', 'quantity']


class CartAdmin(ModelAdmin):
    model = Cart
    list_display = ['id', 'user']
    inlines = [CartItemInlines]


admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
