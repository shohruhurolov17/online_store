from django.contrib import admin
from .models import (
    Category,
    Product
)
from django.contrib.admin import ModelAdmin
# Register your models here.


class ProductAdmin(ModelAdmin):
    model = Product
    list_display = [
       'id', 'category', 'name', 'description', 'price', 'image', 'initial_quantity'
    ]


admin.site.register(Product, ProductAdmin)
