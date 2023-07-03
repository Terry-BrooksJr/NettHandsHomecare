import random

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.us.models import USSocialSecurityNumberField
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField


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

    class EMPLOYMENT_STATUS(models.TextChoices):
        ACTIVE = "A", _("Active")
        TERMINATED = "T", _("Terminated")

    gender = models.CharField(
        max_length=255,
        choices=GENDER.choices,
        default=GENDER.NON_GENDERED,
    )

    social_security = USSocialSecurityNumberField(unique=True, null=True)
    street_address = models.CharField(max_length=255, default="", null=True)
    city = models.CharField(max_length=255, default="", null=True)
    phone = PhoneNumberField(null=True)
    state = USStateField(null=True)
    zipcode = USZipCodeField(null=True)
    pre_service_completion_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(null=True, blank=True)
    hire_date = models.DateField(null=True)
    in_compliance = models.BooleanField(default=False, null=True)

    # TODO: Implement List Field - Lists All Training History (Assessments Model Ref)
    # training_history = models.L

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.username}-{self.job_title})"
