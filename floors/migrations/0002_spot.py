# Generated by Django 4.1.4 on 2022-12-16 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("floors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Spot",
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
                (
                    "variety",
                    models.CharField(
                        choices=[("car", "Car"), ("motorcycle", "Motorcycle")],
                        default="car",
                        max_length=50,
                    ),
                ),
                (
                    "floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spots",
                        to="floors.floor",
                    ),
                ),
            ],
        ),
    ]
