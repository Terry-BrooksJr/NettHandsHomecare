import random

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Assessment(models.Model):
    user = models.ForeignKey("Employee", on_delete=models.CASCADE)
    attempt_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ""


class Employee(AbstractUser):
    class GENDER(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        NON_GENDERED = "X", _("Non-Gendered")
        BINARY = "B", _("Binary")

    gender = models.CharField(
        max_length=255,
        choices=GENDER.choices,
        default=GENDER.NON_GENDERED,
    )
    social_security = models.PositiveIntegerField(
        validators=[MaxValueValidator(999999999)],
        default=00000,
    )
    street_address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")
    zipcode = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)],
        default=00000,
    )
    in_compliance = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.username})"
