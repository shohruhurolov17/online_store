from django.db import models
from category.models import Category
# Create your models here.


class Product(models.Model):
    DoesNotExist = None
    objects = None

    category = models.ForeignKey(
        Category,
        models.CASCADE
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=160)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/')
    initial_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'products'
        unique_together = ['name']

    def __str__(self):
        return self.name
