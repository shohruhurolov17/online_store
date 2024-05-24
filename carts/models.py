from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from products.serializers import ProductSerializer


# Create your models here.


class Cart(models.Model):
    DoesNotExist = None
    objects = None
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    cart_items = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"{self.user}ning savati uchun"

    class Meta:
        db_table = 'carts'
        ordering = ['id']


class CartItem(models.Model):
    objects = None
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(
        Product,
        related_name='card_product',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = 'cart_items'
        unique_together = ['cart', 'product']
        ordering = ['id']




