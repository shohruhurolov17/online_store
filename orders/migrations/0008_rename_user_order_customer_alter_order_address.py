# Generated by Django 4.2 on 2024-03-08 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='Tashkent shahar, chilanzor 21 daha', max_length=150),
        ),
    ]