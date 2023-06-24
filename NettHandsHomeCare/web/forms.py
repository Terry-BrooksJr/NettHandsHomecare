from django import forms
from web.models import ClientInterestSubmissions
class ClientInterestForm(forms.ModelForm):
    """Form definition for ClientInterestSubmission."""

    class Meta:
        """Meta definition for ClientInterestSubmissionform."""

        model = ClientInterestSubmissions
        fields = "__all__"
