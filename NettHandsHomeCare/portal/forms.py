from django import forms
from django.contrib.auth.forms import UserCreationForm
from portal.models import Employee


class SignUpForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ("username", "email")


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
