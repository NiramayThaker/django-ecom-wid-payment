# Generated by Django 4.2.13 on 2024-06-12 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactus", name="desc", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="contactus", name="phone_number", field=models.IntegerField(),
        ),
    ]
