# Generated by Django 5.0.6 on 2024-07-04 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('istok_app', '0002_category_product_productimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10, verbose_name='Цена со скидкой'),
        ),
    ]
