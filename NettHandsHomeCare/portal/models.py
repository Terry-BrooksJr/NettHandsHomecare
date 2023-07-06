import pendulum
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.us.models import USSocialSecurityNumberField
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

now = pendulum.now(tz="America/Chicago")


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

    class MARITAL_STATUS(models.TextChoices):
        MARRIED = "M", _("Married")
        DIVORCED = "D", _("Divorced")
        SEPARATED = "S", _("Separated")
        WIDOWED = "W", _("Widowed")
        NEVER_MARRIED = "NM", _("Never Married")

    class DEPARTMENT(models.TextChoices):
        PATIENT_CARE = "PC", _("Patient Care")
        ADMIN = "A", _("Administration")
        BILLING = "B", _("Billing")
        OTHER = "O", _("Other")

    gender = models.CharField(
        max_length=255,
        choices=GENDER.choices,
        default=GENDER.NON_GENDERED,
    )
    social_security = USSocialSecurityNumberField(unique=True, null=True)
    middle_name = models.CharField(max_length=255, default="")
    street_address = models.CharField(max_length=255, default="", null=True)
    marital_status = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=MARITAL_STATUS.choices,
        default=MARITAL_STATUS.NEVER_MARRIED,
    )
    emergency_contact_first_name = models.CharField(
        max_length=255,
        default="",
        null=True,
    )
    emergency_contact_last_name = models.CharField(
        max_length=255,
        default="",
        null=True,
    )
    emergency_contact_relationship = models.CharField(
        max_length=255,
        default="",
        null=True,
    )
    emergency_contact_phone = PhoneNumberField(default="+15555555555")
    city = models.CharField(max_length=255, default="", null=True)
    department = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        choices=DEPARTMENT.choices,
        default=DEPARTMENT.PATIENT_CARE,
    )
    phone = PhoneNumberField(null=True)
    state = USStateField(null=True)
    zipcode = USZipCodeField(null=True)
    pre_service_completion_date = models.DateField(null=True, blank=True)
    job_title = models.CharField(null=True, max_length=255, blank=True)
    hire_date = models.DateField(null=True)
    in_compliance = models.BooleanField(default=False, null=True)
    onboarded = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"(Employee Id:{self.id}), Name: {self.last_name}, {self.first_name} | Username: {self.username}| Title: {self.job_title})"

    def onboarding_complete(self):
        valid_fields = 0
        fields_to_be_validated = [
            self.social_security,
            self.gender,
            self.city,
            self.phone,
            self.state,
            self.street_address,
            self.zipcode,
            self.emergency_contact_relationship,
            self.emergency_contact_last_name,
            self.emergency_contact_first_name,
            self.marital_status,
        ]
        for field in fields_to_be_validated:
            if field is not None or field != " ":
                valid_fields += 1

        if valid_fields == 10:
            self.onboarded = now
            return True
        else:
            return False
