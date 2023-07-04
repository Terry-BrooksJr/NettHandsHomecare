from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button
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
            "id",
            "social_security",
            "street_address",
            "city",
            "phone",
            "gender",
            "state",
            "zipcode",
            "job_title",
            "hire_date",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                """
        <h6 class="small-heading muted-text mb-4">User Information</strong></h6>
        <div class="pl-lg-4">

        """,
            ),
            Row(
                Column(
                    "username",
                    readonly=True,
                    css_class="form-group col-md-6 mb-0 ",
                ),
                Column(
                    "email",
                    readonly=True,
                    css_class="form-group col-md-6 mb-0  editable",
                ),
                css_class="form-row ",
            ),
            Row(
                Column(
                    "first_name",
                    readonly=True,
                    css_class="form-group col-md-6 mb-0  editable",
                ),
                Column(
                    "last_name",
                    readonly=True,
                    css_class="form-group col-md-6 mb-0  editable",
                ),
                css_class="form-row",
            ),
            Row(
                Column(
                    "hire_date",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                Column("id", readonly=True, css_class="form-group col-lg-4 mb-0"),
                Column(
                    "job_title",
                    readonly=True,
                    css_class="form-group col-lg-4 mb-0",
                ),
                css_class="form-row ",
            ),
            HTML("""</div> """),
            HTML("""<hr class="my-4 />"""),
            HTML(
                """
        <h6 class="small-heading muted-text mb-4">Contact Information</strong></h6>
        <div class="pl-lg-4">

        """
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
            Row(
                FormActions(Submit("save", "Save changes"), Button("cancel", "Cancel")),
                css_class="form-row",
            ),
        )
