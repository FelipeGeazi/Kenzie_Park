# Generated by Django 4.1.4 on 2022-12-15 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("parking_lots", "0002_parkinglot_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="Floor",
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
                ("name", models.CharField(max_length=127)),
                ("spot_priority", models.IntegerField()),
                (
                    "parking_lot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="floors",
                        to="parking_lots.parkinglot",
                    ),
                ),
            ],
        ),
    ]
