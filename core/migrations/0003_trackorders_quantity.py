# Generated by Django 4.2.13 on 2024-06-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_trackorders_desc"),
    ]

    operations = [
        migrations.AddField(
            model_name="trackorders",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
