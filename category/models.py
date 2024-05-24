from django.db import models


# Create your models here.


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=120)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'categories'
        unique_together = ['name']
