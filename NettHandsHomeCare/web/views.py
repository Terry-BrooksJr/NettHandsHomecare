import json
import os
import pprint
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from string import Template

from django.shortcuts import redirect
from django.shortcuts import render
from dotenv import load_dotenv
from web.forms import ClientInterestForm
from web.forms import EmploymentApplicationForm
from web.utils import application_body
from web.utils import client_body

load_dotenv()
# SECTION - Page Rendering Views


def index(request):
    """Primary Render Function that Renders the Homepage template located in index.html.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling.

    Returns:
        Renders Homepage
    """
    return render(request, "index.html", {"title": "Home"})


def about(request):
    """Primary Render Function that Renders the about sub-page template located in contact.html.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling.

    Returns:
        Renders Contact Subpage
    """
    return render(request, "about.html", {"title": "About Nett Hands"})


#!SECTION

# SECTION - Internal Functional View


def send_external_application_submission_confirmation(form):
    """Class method to send email notification of the submissions of client interest and employment application forms

    Args:
        form: Form Instance
    """
    try:
        sender_email = os.getenv("NOTIFICATION_SENDER_EMAIL")
        sender_password = os.getenv("EMAIL_ACCT_PASSWORD")
        recipient_email = form.cleaned_data["email"].lower()
        subject = (
            f"Thanks For Your Employment Interest, {form.cleaned_data['first_name']}!"
        )
        content = application_body

        html_message = MIMEText(content, "html")
        html_message["Subject"] = subject
        html_message["From"] = sender_email
        html_message["To"] = recipient_email
        with smtplib.SMTP_SSL(
            os.getenv("EMAIL_SERVER"),
            os.getenv("EMAIL_SSL_PORT"),
        ) as server:
            server.login(sender_email, sender_password)
            return server.sendmail(
                sender_email,
                recipient_email,
                html_message.as_string(),
            )
    except Exception as e:
        return str(e)


def send_internal_application_submission_confirmation(form):
    """Internal Non-Rendering View Function to send email notification of the submissions of client interest and employment application forms"""
    try:
        sender_email = os.getenv("NOTIFICATION_SENDER_EMAIL")
        recipient_email = os.getenv("NOTIFICATION_Application_SUBMISSION_EMAIL")
        sender_password = os.getenv("EMAIL_ACCT_PASSWORD")
        subject = f"New Employment Interest - {form.cleaned_data['last_name']}, {form.cleaned_data['first_name']}"
        message = EmailMessage()
        message["Subject"] = subject
        message["To"] = recipient_email
        content_template = Template(
            """
            Attention: A New Employment Interest has Been Submitted, the application information is as follows: \n
            First Name: $first_name\n
            Last Name: $last_name\n
            E-mail: $email\n
            Contact Number: $contact_number\n
            Street Address: $home_address\n
            City: $city\n
            State: $state\n
            Zipcode: $zipcode\n
            Mobility: $mobility\n
            Prior Expierence: $prior_experience\n
            Available Monday: $availability_monday\n
            Availability Tuesday: $availability_tuesday\n
            Availability Wednesday: $availability_wednesday\n
            Availability Thursday: $availability_thursday\n
            Availability Friday: $availability_friday\n
            Availability Saturday: $availability_saturday\n
            Availability Sunday: $availability_sunday\n
            """,
        )
        content = content_template.substitute(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"],
            contact_number=form.cleaned_data["contact_number"],
            home_address=form.cleaned_data["home_address"],
            city=form.cleaned_data["city"],
            state=form.cleaned_data["state"],
            zipcode=form.cleaned_data["zipcode"],
            mobility=form.cleaned_data["mobility"],
            prior_experience=form.cleaned_data["prior_experience"],
            availability_monday=form.cleaned_data["availability_monday"],
            availability_tuesday=form.cleaned_data["availability_tuesday"],
            availability_wednesday=form.cleaned_data["availability_wednesday"],
            availability_thursday=form.cleaned_data["availability_thursday"],
            availability_friday=form.cleaned_data["availability_friday"],
            availability_saturday=form.cleaned_data["availability_saturday"],
            availability_sunday=form.cleaned_data["availability_sunday"],
        )
        server_ssl = smtplib.SMTP_SSL(
            os.getenv("EMAIL_SERVER"),
            os.getenv("EMAIL_SSL_PORT"),
        )
        server_ssl.ehlo()
        server_ssl.login(
            os.getenv("NOTIFICATION_SENDER_EMAIL"),
            os.getenv("EMAIL_ACCT_PASSWORD"),
        )
        message.set_content(content)
        server_ssl.send_message(message)
        server_ssl.quit()
    except Exception as e:
        return f"Something went wrong...{e}"


def send_external_client_submission_confirmation(form):
    """Internal Non-Rendering View Function to send email notification of the submissions of client interest and employment application forms

    Args:
        form: Form Instance
    """
    try:
        sender_email = os.getenv("NOTIFICATION_SENDER_EMAIL")
        sender_password = os.getenv("EMAIL_ACCT_PASSWORD")
        recipient_email = form.cleaned_data["email"].lower()
        subject = f"We Got Your Client Interest {form.cleaned_data['first_name']}!"
        content = client_body

        html_message = MIMEText(content, "html")
        html_message["Subject"] = subject
        html_message["From"] = sender_email
        html_message["To"] = recipient_email
        with smtplib.SMTP_SSL(
            os.getenv("EMAIL_SERVER"),
            os.getenv("EMAIL_SSL_PORT"),
        ) as server:
            server.login(sender_email, sender_password)
            return server.sendmail(
                sender_email,
                recipient_email,
                html_message.as_string(),
            )
    except Exception as e:
        return str(e)


def send_internal_client_submission_confirmation(form):
    """Internal Non-Rendering View Function to send email notification of the submissions of client interest and employment application forms
    Args:
        form: Form Instance
    """
    try:
        sender_email = os.getenv("NOTIFICATION_SENDER_EMAIL")
        recipient_email = os.getenv("NOTIFICATION_CLIENT_SUBMISSION_EMAIL")
        sender_password = os.getenv("EMAIL_ACCT_PASSWORD")
        subject = f"New Client Interest - {form.cleaned_data['last_name']}, {form.cleaned_data['first_name']}"
        message = EmailMessage()
        message["Subject"] = subject
        message["To"] = recipient_email
        content_template = Template(
            """
            Attention: A New Client Interest has Been Submitted, the application information is as follows: \n
            First Name: $first_name\n
            Last Name: $last_name\n
            E-mail: $email\n
            Contact Number: $contact_number\n
            Zipcode: $zipcode\n
            Insurance Carrier: $insurance_carrier\n
            Desired Service: $desired_service
            """,
        )
        content = content_template.substitute(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            email=form.cleaned_data["email"],
            desired_service=form.cleaned_data["desired_service"],
            contact_number=form.cleaned_data["contact_number"],
            zipcode=form.cleaned_data["zipcode"],
            insurance_carrier=form.cleaned_data["insurance_carrier"],
        )
        server_ssl = smtplib.SMTP_SSL(
            os.getenv("EMAIL_SERVER"),
            os.getenv("EMAIL_SSL_PORT"),
        )
        server_ssl.ehlo()
        server_ssl.login(
            os.getenv("NOTIFICATION_SENDER_EMAIL"),
            os.getenv("EMAIL_ACCT_PASSWORD"),
        )
        message.set_content(content)
        server_ssl.send_message(message)
        server_ssl.quit()
    except Exception as e:
        return f"Something went wrong...{e}"


# !SECTION
# SECTION - Form Processing Views
def client_interest(request):
    """Instantiates the ClientInterestForm Class and checks the request.method. If Post - Processes Form Data. If GET - Renders Form

    Args:
        request (object): Request Object Passed at time of calling.

    Returns:
        Renders wor Processes ClientInterestForm
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ClientInterestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ic(send_external_client_submission_confirmation(form))
            ic(send_internal_client_submission_confirmation(form))
            return redirect("submitted")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ClientInterestForm()

    return render(
        request,
        "client-interest.html",
        {"form": form, "title": "Client Interest Form"},
    )


def employee_interest(request):
    """Secondary Render Function that Renders the sub-page for the employee interest form template located in 'employee-interest.html' file.

    Args:
        request (HttpRequestObject): Request Object Passed at time of calling.

    Returns:
        Renders sub-page Employee Application Form
    """
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EmploymentApplicationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            ic(send_internal_application_submission_confirmation(form))
            ic(send_external_application_submission_confirmation(form))
            return redirect("submitted")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EmploymentApplicationForm()

    return render(
        request,
        "employee-interest.html",
        {"form": form, "title": "Employment Application"},
    )


def submitted(request):
    return render(request, "submission.html", {"title": "Form Submission Confirmation"})


#!SECTION
