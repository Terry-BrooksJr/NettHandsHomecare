from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column
from crispy_forms.layout import HTML
from crispy_forms.layout import Layout
from crispy_forms.layout import Reset
from crispy_forms.layout import Row
from crispy_forms.layout import Submit
from django import forms
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from portal.models import Contract
from portal.models import Employee


class ContractForm(forms.ModelForm):
    """Form definition for Employee Model."""

    class Meta:
        """Meta definition for EmployeeForm."""

        model = Contract
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    """Form definition for Employee Model."""

    class Meta:
        """Meta definition for EmployeeForm."""

        model = Employee
        fields = (
            "gender",
            "social_security",
            "middle_name",
            "street_address",
            "last_name",
            "first_name",
            "marital_status",
            "emergency_contact_first_name",
            "emergency_contact_last_name",
            "emergency_contact_relationship",
            "emergency_contact_phone",
            "city",
            "email",
            "department",
            "phone",
            "state",
            "zipcode",
            "pre_service_completion_date",
            "job_title",
            "aps_check_passed",
            "ethnicity",
            "family_hca",
            "hhs_oig_exclusionary_check_completed",
            "hhs_oig_exclusionary_check_verification",
            "language",
            "cpr_verification",
            "pre_training_verification",
            "qualifications",
            "race",
            "qualifications_verification",
            "contract_code",
            "username",
        )
        labels = {
            "language": _(
                "Language Preference",
            ),
            "family_hca": _("Are You Related By Blood or Marriage to your patient?"),
            "qualifications": _(
                "Highest Level of Education/Home Healthcare Qualification",
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse("profile")
        self.helper.form_id = "profile"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            HTML(
                """
        <h6 class="small-heading muted-text mb-4">User Information</strong></h6>
        <div class="pl-lg-4">
        """,
            ),
            Row(
                Column(
                    "email",
                    disabled=True,
                    css_class="form-group col-md-6 mb-0  editable",
                ),
                css_class="form-row ",
            ),
            Row(
                Column(
                    "first_name",
                    readonly=True,
                    css_class="form-group col-md-4 mb-0  editable",
                ),
                Column(
                    "middle_name",
                    readonly=True,
                    css_class="form-group col-md-4 mb-0  editable",
                ),
                Column(
                    "last_name",
                    readonly=True,
                    css_class="form-group col-md-44 mb-0  editable",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "hire_date",
                    editable=False,
                    css_class="form-group col-lg-4 mb-0",
                ),
                Column(
                    "job_title",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                Column(
                    "department",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                css_class="form-row ",
            ),
            Row(
                Column(
                    "language",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                Column(
                    "ethnicity",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                Column(
                    "race",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                css_class="form-row ",
            ),
            Row(
                Column("family_hca", css_class="form-group col-md-12 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("qualifications", css_class="form-group col-md-12 mb-0"),
                css_class="form-row",
            ),
            HTML("""</div> """),
            HTML("""<hr class="my-4 />"""),
            HTML(
                """
        <h6 class="small-heading muted-text mb-4">Contact Information</strong></h6>
        <div class="pl-lg-4">

        """,
            ),
            Row(
                Column(
                    "street_address",
                    readonly=True,
                    css_class="form-group col-md-12 mb-0 editable   ",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "city",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "state",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "zipcode",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "phone",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "social_security",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "gender",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            HTML("""</div> """),
            HTML("""<hr class="my-4 />"""),
            HTML(
                """
        <h6 class="small-heading muted-text mb-4">Emergency Contact</strong></h6>
        <div class="pl-lg-4">

        """,
            ),
            Row(
                Column(
                    "emergency_contact_first_name",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "emergency_contact_last_name",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "emergency_contact_phone",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "emergency_contact_relationship",
                    readonly=True,
                    css_class="form-group col-lg-8 mb-0 editable ",
                ),
                css_class="form-row",
            ),
            HTML("""<hr class="my-4 />"""),
            HTML(
                """
        <h6 class="small-heading muted-text mb-4">Supporting Documentation</strong></h6>
        <div class="pl-lg-4">

        """,
            ),
            Row(
                Column(
                    "hhs_oig_exclusionary_check_verification",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "pre_training_verification",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ),
                Column(
                    "qualifications_verification",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0 editable ",
                ), 
                css_class="form-row",
            ),
            Row(
                FormActions(
                    Submit("save", "Save changes", id="edit-button"),
                    Reset(
                        "cancel",
                        "Cancel",
                        css_class="btn btn-danger",
                        id="cancel-edits-btn",
                    ),
                ),
                css_class="form-row",
            ),
        )
