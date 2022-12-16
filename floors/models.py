from django.db import models


class Floor(models.Model):
    name = models.CharField(max_length=127)
    spot_priority = models.IntegerField()

    # 1:N -> ParkingLot -> Floor
    parking_lot = models.ForeignKey(
        "parking_lots.ParkingLot",
        on_delete=models.CASCADE,
        related_name="floors",
    )


class SpotType(models.TextChoices):
    CAR = "car"
    MOTORCYCLE = "motorcycle"


class Spot(models.Model):
    variety = models.CharField(
        max_length=50,
        choices=SpotType.choices,
        default=SpotType.CAR,
    )

    # 1:N - Floor -> Spot
    floor = models.ForeignKey(
        "floors.Floor",
        on_delete=models.CASCADE,
        related_name="spots",
    )
