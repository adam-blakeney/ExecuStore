# Generated by Django 3.2 on 2022-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20221122_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
