# Generated by Django 4.2.13 on 2024-06-12 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_auth", "0006_alter_product_image"),
    ]

    operations = [
        migrations.DeleteModel(name="Product",),
    ]
