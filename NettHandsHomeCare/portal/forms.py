from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column
from crispy_forms.layout import HTML
from crispy_forms.layout import Layout
from crispy_forms.layout import Row
from crispy_forms.layout import Submit
from django import forms
from django.utils.translation import gettext_lazy as _
from portal.models import Employee


class EmployeeForm(forms.ModelForm):
    """Form definition for Employee Model."""

    class Meta:
        """Meta definition for EmployeeForm."""

        model = Employee
        fields = (
            "social_security",
            "street_address",
            "city",
            "phone",
            "state",
            "zipcode",
            "job_title",
            "hire_date",
        )
