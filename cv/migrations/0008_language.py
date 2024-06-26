# Generated by Django 4.2.13 on 2024-06-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0007_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=254)),
            ],
        ),
    ]
