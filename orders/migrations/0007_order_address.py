# Generated by Django 4.2 on 2024-02-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_products_order_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Tashkent shahar, yunusobod', max_length=150),
        ),
    ]
