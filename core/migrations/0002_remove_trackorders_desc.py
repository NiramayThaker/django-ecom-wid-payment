# Generated by Django 4.2.13 on 2024-06-22 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="trackorders", name="desc",),
    ]