# Generated by Django 3.1.7 on 2021-03-12 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210312_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
    ]
