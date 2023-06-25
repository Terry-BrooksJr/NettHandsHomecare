from django import forms
from web.models import ClientInterestSubmissions, EmploymentApplicationModel


class ClientInterestForm(forms.ModelForm):
    """Form definition for ClientInterestSubmission."""

    class Meta:
        """Meta definition for ClientInterestSubmissionform."""

        model = ClientInterestSubmissions
        fields = (
            "first_name",
            "last_name",
            "contact_number",
            "zipcode",
            "insurance_carrier",
            "desired_service",
        )


class EmploymentApplicationForm(forms.ModelForm):
    """Form definition for EmploymentApplicationModel."""

    class Meta:
        """Meta definition for EmploymentApplicationModelForm."""

        model = EmploymentApplicationModel
        fields = (
            "first_name",
            "last_name",
            "contact_number",
            "email",
            "home_address",
            "city",
            "state",
            "zipcode",
            "mobility",
            "prior_experience",
            "availability_monday",
            "availability_tuesday",
            "availability_wednesday",
            "availability_thursday",
            "availability_friday",
            "availability_saturday",
            "availability_sunday",
        )
