from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.us.models import USStateField
from localflavor.us.models import USZipCodeField
from pendulum import now
from phonenumber_field.modelfields import PhoneNumberField

now = now(tz="America/Chicago")


class ClientInterestSubmissions(models.Model):
    class SERVICES(models.TextChoices):
        INTERMITTENT = "I", _("Intermittent Home Care")
        NONMEDICAL = "NM", _("Non-Medical Home Care")
        MEDICAL_SW = "MSW", _("Medical Social Work")
        OCCUP_THERAPY = "OT", _("Occupational Therapy")
        PHYS_THERAPY = "PT", _("Physical Therapy")
        OTHER = "NA", _("Other")

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    contact_number = PhoneNumberField(region="US")
    zipcode = USZipCodeField()
    insurance_carrier = models.CharField(max_length=255)
    desired_service = models.CharField(max_length=255, choices=SERVICES.choices)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} - Submission Date: {self.date_submitted}"

    class Meta:
        db_table = "interest_clients"
        ordering = ["last_name", "first_name", "date_submitted"]
        verbose_name = "Interested Client"
        verbose_name_plural = "Interested Clients"


class EmploymentApplicationModel(models.Model):
    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.id}) - Submitted:{self.date_submitted}"

    class MOBILITTY(models.TextChoices):
        CAR = "C", _("I Have Consistent Access To A Car")
        PUBLIC = "P", _("I Use Public Transportation")
        RIDE_SHARE = "RS", _(
            "I Use Rideshare (Uber/Lyft) or a Reliable Pickup/Dropoff Provider",
        )
        OTHER = "NA", _("Other")

    class PRIOREXPERIENCE(models.TextChoices):
        SENIOR = "S", _("12+ Months")
        JUNIOR = "J", _("3+ Months")
        NEW = "N", _("No Prior Experience")

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number = PhoneNumberField(region="US")
    email = models.EmailField(max_length=254)
    home_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = USStateField(max_length=2)
    zipcode = USZipCodeField()
    mobility = models.CharField(max_length=255, choices=MOBILITTY.choices)
    prior_experience = models.CharField(max_length=255, choices=PRIOREXPERIENCE.choices)
    ipdh_registered = models.BooleanField(default=False)
    availability_monday = models.BooleanField()
    availability_tuesday = models.BooleanField()
    availability_wednesday = models.BooleanField()
    availability_thursday = models.BooleanField()
    availability_friday = models.BooleanField()
    availability_saturday = models.BooleanField()
    availability_sunday = models.BooleanField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "employment_interests"
        ordering = ["last_name", "first_name", "date_submitted"]
        verbose_name = "Prospective Employee"
        verbose_name_plural = "Prospective Employees"
