from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.


class Order(models.Model):
    status = models.CharField(
        max_length=8,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('rejected', 'Rejected'),
        ],
        default='pending'
    )

    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default='Tashkent shahar, chilanzor 21 daha')
    order_items = models.ManyToManyField(Product, through='OrderItem')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    objects = None
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return str(self.product)

    class Meta:
        db_table = 'order_items'
