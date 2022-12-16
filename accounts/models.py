from django.db import models
from django.contrib.auth.models import AbstractUser


class ShiftOptions(models.TextChoices):
    MORNING = "Matutino"
    AFTERNOON = "Vespertino"
    NIGHT = "Noturno"
    DEFAULT = "Não informado"


class Account(AbstractUser):
    shift = models.CharField(
        max_length=50,
        choices=ShiftOptions.choices,
        default=ShiftOptions.DEFAULT,
        null=True,
    )
    email = models.EmailField(max_length=127, unique=True)
