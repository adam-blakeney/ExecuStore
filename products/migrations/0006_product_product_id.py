# Generated by Django 3.2 on 2022-12-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]