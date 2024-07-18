# Generated by Django 5.0.6 on 2024-07-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('istok_app', '0003_alter_product_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой'),
        ),
    ]