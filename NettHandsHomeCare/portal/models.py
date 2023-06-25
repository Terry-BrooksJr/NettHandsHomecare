import random

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

    _employee_id = models.CharField(max_length=255, primary_key=True)
    gender = models.CharField(max_length=255, choices=GENDER.choices)
    social_security = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.employee_id})"

    def create_employee_id(self):
        emp_id = list()
        emp_id.append(self.first_name[0].upper())
        emp_id.append(self.last_name[0].upper())
        emp_id.append(str(random.randint(00000, 99999)))
        emp_id = "".join(emp_id)
        return emp_id

    def assign_employee_id(self):
        emp_id = self.create_employee_id()
        employees = self.objects.all()
        if emp_id in employees["emp_id"]:
            self.assign_employee_id()
        else:
            self._employee_id = emp_id
