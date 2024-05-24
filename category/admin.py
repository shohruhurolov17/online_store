from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
# Register your models here.
from .models import Category
from products.models import Product


class ProductAdmin(TabularInline):
    model = Product
    extra = 0


class CategoryAdmin(ModelAdmin):
    inlines = [ProductAdmin]


admin.site.register(Category, CategoryAdmin)