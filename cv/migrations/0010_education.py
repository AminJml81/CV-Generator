# Generated by Django 4.2.13 on 2024-06-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0009_skill"),
    ]

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("university", models.CharField(max_length=150)),
                ("major", models.CharField(max_length=100)),
                ("degree", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("graduation_date", models.DateField()),
            ],
        ),
    ]
