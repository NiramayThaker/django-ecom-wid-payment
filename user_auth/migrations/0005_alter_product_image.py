# Generated by Django 4.2.13 on 2024-06-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_auth", "0004_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default="", upload_to="images/images"),
        ),
    ]
