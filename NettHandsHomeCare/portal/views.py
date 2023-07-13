import csv
import json
import os

import pendulum
from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.template import loader
from django.urls import reverse
from django.views.generic.detail import DetailView
from icecream import ic
from portal.forms import EmployeeForm
from portal.models import Employee
from web.forms import ClientInterestForm
from web.models import ClientInterestSubmissions, EmploymentApplicationModel

now = pendulum.now(tz="America/Chicago")


@login_required(login_url="/login/")
def index(request):
    context = {"segment": "index"}

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def profile_view(request):
    context = dict()
    context["data"] = Employee.objects.get(id=request.user.id)
    user = context["data"]
    init_values = {
        "id": user.id,
        "social_security": user.social_security,
        "street_address": user.street_address,
        "city": user.city,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "username": user.username,
        "emergency_contact_first_name": user.emergency_contact_first_name,
        "emergency_contact_last_name": user.emergency_contact_last_name,
        "emergency_contact_phone": user.emergency_contact_phone,
        "phone": user.phone,
        "gender": user.gender,
        "middle_name": user.middle_name,
        "state": user.state,
        "zipcode": user.zipcode,
        "job_title": user.job_title,
        "hire_date": user.hire_date,
    }
    context["form"] = EmployeeForm(initial=init_values)
    return render(request=request, template_name="home/profile.html", context=context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    ic(context)
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split("/")[-1]

        if load_template == "admin":
            return HttpResponseRedirect(reverse("admin:index"))
        context["segment"] = load_template

        html_template = loader.get_template("home/" + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template("home/page-404.html")
        return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template("home/page-500.html")
    #     return HttpResponse(html_template.render(context, request))


def send_new_user_credentials(new_user):
    """Internal Non-Rendering View Function to send email notification of user namne and password"""
    try:
        sender_email = os.getenv("NOTIFICATION_SENDER_EMAIL")
        recipient_email = new_user.email
        sender_password = os.getenv("EMAIL_ACCT_PASSWORD")
        subject = f"Welcome to Nett Hands - {new_user.first_name}!"
        message = EmailMessage()
        message["Subject"] = subject
        message["To"] = recipient_email
        content_template = Template(
            f"""
            Welcome to Nett Hands, Please Login Your New Employee Account at https://www.netthandshome.care/login/ and Complete Onboarding Information in the Personal Information Section:

            Username = $username
            Password = $password
            """,
        )
        content = content_template.substitute(
            username=new_user.first_name,
            password=new_user.password,
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


@login_required(login_url="/login/")
def profile(request):
    context = dict()
    context["data"] = Employee.objects.get(id=request.user.id)
    user = context["data"]
    init_values = {
        "id": user.id,
        "social_security": user.social_security,
        "street_address": user.street_address,
        "city": user.city,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "username": user.username,
        "emergency_contact_first_name": user.emergency_contact_first_name,
        "emergency_contact_last_name": user.emergency_contact_last_name,
        "emergency_contact_phone": user.emergency_contact_phone,
        "phone": user.phone,
        "gender": user.gender,
        "middle_name": user.middle_name,
        "state": user.state,
        "zipcode": user.zipcode,
        "job_title": user.job_title,
        "emergency_contact_relationship": user.emergency_contact_relationship,
        "hire_date": user.hire_date,
        "aps_check_passed": user.aps_check_passed,
        "aps_check_verification": user.aps_check_verification,
        "cpr_verification": user.cpr_verification,
        "family_hca": user.family_hca,
        "hhs_oig_exclusionary_check_completed": user.hhs_oig_exclusionary_check_completed,
        "hhs_oig_exclusionary_check_verification": user.hhs_oig_exclusionary_check_verification,
        "language": user.language,
        "pre_training_verification": user.pre_training_verification,
        "qualifications": user.qualifications,
        "qualifications_verification": user.qualifications_verification,
        "training_exempt": user.training_exempt,
    }

    if request.method == "POST":
        user = Employee.objects.get(username=request.user.username)
        form = EmployeeForm(request.POST, request.FILES)
        user.aps_check_passed = form.data.get("aps_check_passed")
        user.cpr_verification = form.data.get("cpr_verification")
        user.family_hca = form.data.get("family_hca")
        user.hhs_oig_exclusionary_check_completed = form.data.get(
            "hhs_oig_exclusionary_check_completed",
        )
        user.hhs_oig_exclusionary_check_verification = form.data.get(
            "hhs_oig_exclusionary_check_verification",
        )
        user.language = form.data.get("language")
        user.pre_training_verification = form.data.get("pre_training_verification")
        user.qualifications = form.data.get("qualifications")
        user.social_security = form.data.get("social_security")
        user.street_address = form.data.get("street_address")
        user.phone = form.data.get("phone")
        user.qualifications_verification = form.data.get("qualifications_verification")
        user.zipcode = form.data.get("zipcode")
        user.middle_name = form.data.get("middle_name")
        user.emergency_contact_relationship = form.data.get(
            "emergency_contact_relationship",
        )
        user.email = form.data.get("email")
        user.emergency_contact_first_name = form.data.get(
            "emergency_contact_first_name",
        )
        user.first_name = form.data.get("first_name")
        user.last_name = form.data.get("last_name")
        user.city = form.data.get("city")
        user.state = form.data.get("state")
        user.department = form.data.get("department")
        user.gender = form.data.get("gender")
        user.save()
        return redirect(reverse("profile"))

    elif request.method == "GET":
        context["form"] = EmployeeForm(initial=init_values)
        return render(
            request=request,
            template_name="home/profile.html",
            context=context,
        )


def all_client_inquiries(request):
    inquiries = ClientInterestSubmissions.objects.all().values()
    inquiries_json = json.dumps(list(inquiries), cls=DjangoJSONEncoder)
    return HttpResponse(content=inquiries_json, status=200)


@login_required(login_url="/login/")
def client_inquiries(request):
    context = dict()
    context["submissions"] = ClientInterestSubmissions.objects.all().order_by(
        "-date_submitted",
    )
    countUnresponsed = ClientInterestSubmissions.objects.filter(reviewed=False).count()
    context["unresponsed"] = countUnresponsed
    context["showSearch"] = True
    context["reviewed"] = ClientInterestSubmissions.objects.filter(
        reviewed=True,
    ).count()
    context["all_submuission"] = ClientInterestSubmissions.objects.all().count
    return render(request, "home/service-inquiries.html", context)


@login_required(login_url="/login/")
def submission_detail(request, pk):
    context = dict()
    submission = ClientInterestSubmissions.objects.get(pk=pk)
    context["type"] = "Client Interest"
    init_values = {
        "id": submission.id,
        "first_name": submission.first_name,
        "last_name": submission.last_name,
        "email": submission.email,
        "contact_number": submission.contact_number,
        "zipcode": submission.zipcode,
        "insurance_carrier": submission.insurance_carrier,
        "desired_service": submission.desired_service,
        "date_submitted": submission.date_submitted,
        "reviewed": submission.reviewed,
        "reviewed_by": submission.reviewed_by,
    }
    # context["form"] = ClientInterestForm(initial=init_values)
    context["submission"] = init_values

    return render(request, "home/submission-details.html", context)


def marked_reviewed(request):
    try:
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        pk = body["pk"]
        submission = ClientInterestSubmissions.objects.get(id=pk)
        submission.marked_reviewed(request.user)
        submission.save()
        return HttpResponse(status=204)
    except Exception as e:
        ic(e)
        return HttpResponse(status=418)


@login_required(login_url="/login/")
def employment_applications(request):
    context = dict()
    context["submissions"] = EmploymentApplicationModel.objects.all().order_by(
        "-date_submitted",
    )
    countUnresponsed = EmploymentApplicationModel.objects.filter(reviewed=False).count()
    context["unresponsed"] = countUnresponsed
    context["showSearch"] = True
    context["reviewed"] = EmploymentApplicationModel.objects.filter(
        reviewed=True,
    ).count()
    context["all_submuission"] = EmploymentApplicationModel.objects.all().count
    return render(request, "home/submitted-applications.html", context)


@login_required(login_url="/login/")
def applicant_details(request, pk):
    context = dict()
    submission = EmploymentApplicationModel.objects.get(pk=pk)
    context["type"] = "Client Interest"
    init_values = {
        "id": submission.id,
        "first_name": submission.first_name,
        "last_name": submission.last_name,
        "contact_number": submission.contact_number,
        "email": submission.email,
        "home_address": submission.home_address,
        "city": submission.city,
        "state": submission.state,
        "zipcode": submission.zipcode,
        "mobility": submission.mobility,
        "prior_experience": submission.prior_experience,
        "ipdh_registered": submission.ipdh_registered,
        "availability_monday": submission.availability_monday,
        "availability_tuesday": submission.availability_tuesday,
        "availability_wednesday": submission.availability_wednesday,
        "availability_thursday": submission.availability_thursday,
        "availability_friday": submission.availability_friday,
        "availability_saturday": submission.availability_saturday,
        "availability_sunday": submission.availability_sunday,
        "reviewed": submission.reviewed,
        "hired": submission.hired,
        "reviewed_by": submission.reviewed_by,
        "date_submitted": submission.date_submitted,
    }
    # context["form"] = ClientInterestForm(initial=init_values)
    context["submission"] = init_values

    return render(request, "home/applicant-details.html", context)


def hire(request):
    try:
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        pk = body["pk"]
        submission = EmploymentApplicationModel.objects.get(pk=pk)
        submission.hire(request.user)
        send_new_user_credentials(submission)
        submission.save()
        return HttpResponse(status=201)
    except Exception as e:
        ic(e)
        return HttpResponse(status=418)


def reject(request):
    try:
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        pk = body["pk"]
        submission = EmploymentApplicationModel.objects.get(id=pk)
        submission.reject(request.user)
        submission.save()
        return HttpResponse(status=204)
    except Exception as e:
        return HttpResponse(status=418)


def all_applicants(request):
    inquiries = EmploymentApplicationModel.objects.all().values()
    applicant_json = json.dumps(list(inquiries), cls=DjangoJSONEncoder)
    return HttpResponse(content=applicant_json, status=200)


def employee_roster(request):
    context = dict()
    employees = Employee.objects.all().order_by("last_name")
    context["employees"] = employees
    context["showSearch"] = True
    return render(request, "home/employee-listing.html", context)


def create_contract(request):
    pass


def employee_details(request, pk):
    context = dict()
    context["data"] = Employee.objects.get(id=pk)
    user = context["data"]
    init_values = {
        "id": user.id,
        "social_security": user.social_security,
        "street_address": user.street_address,
        "city": user.city,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "username": user.username,
        "emergency_contact_first_name": user.emergency_contact_first_name,
        "emergency_contact_last_name": user.emergency_contact_last_name,
        "emergency_contact_phone": user.emergency_contact_phone,
        "phone": user.phone,
        "gender": user.gender,
        "middle_name": user.middle_name,
        "state": user.state,
        "zipcode": user.zipcode,
        "job_title": user.job_title,
        "emergency_contact_relationship": user.emergency_contact_relationship,
        "hire_date": user.hire_date,
        "aps_check_passed": user.aps_check_passed,
        "aps_check_verification": user.aps_check_verification,
        "cpr_verification": user.cpr_verification,
        "family_hca": user.family_hca,
        "hhs_oig_exclusionary_check_completed": user.hhs_oig_exclusionary_check_completed,
        "hhs_oig_exclusionary_check_verification": user.hhs_oig_exclusionary_check_verification,
        "language": user.language,
        "pre_training_verification": user.pre_training_verification,
        "qualifications": user.qualifications,
        "qualifications_verification": user.qualifications_verification,
        "training_exempt": user.training_exempt,
    }
    if request.method == "POST":
        user = Employee.objects.get(id=pk)
        form = EmployeeForm(request.POST, request.FILES)
        user.aps_check_passed = form.data.get("aps_check_passed")
        user.cpr_verification = form.data.get("cpr_verification")
        user.family_hca = form.data.get("family_hca")
        user.hhs_oig_exclusionary_check_completed = form.data.get(
            "hhs_oig_exclusionary_check_completed",
        )
        user.hhs_oig_exclusionary_check_verification = form.data.get(
            "hhs_oig_exclusionary_check_verification",
        )
        user.language = form.data.get("language")
        user.pre_training_verification = form.data.get("pre_training_verification")
        user.qualifications = form.data.get("qualifications")
        user.social_security = form.data.get("social_security")
        user.street_address = form.data.get("street_address")
        user.phone = form.data.get("phone")
        user.qualifications_verification = form.data.get("qualifications_verification")
        user.zipcode = form.data.get("zipcode")
        user.middle_name = form.data.get("middle_name")
        user.emergency_contact_relationship = form.data.get(
            "emergency_contact_relationship",
        )
        user.email = form.data.get("email")
        user.emergency_contact_first_name = form.data.get(
            "emergency_contact_first_name",
        )
        user.first_name = form.data.get("first_name")
        user.last_name = form.data.get("last_name")
        user.city = form.data.get("city")
        user.state = form.data.get("state")
        user.department = form.data.get("department")
        user.gender = form.data.get("gender")
        user.save()
        return redirect(reverse("profile"))

    elif request.method == "GET":
        context["form"] = EmployeeForm(initial=init_values)
        return render(
            request=request,
            template_name="home/profile.html",
            context=context,
        )


def employee_report_export():
    employees = Employee.objects.all().values()
    employee_json = json.dumps(list(employees), cls=DjangoJSONEncoder)
    return HttpResponse(content=employee_json, status=200)


def generate_report(requst):
    sessionDataCSV = f"TTPUpload{now.to_date_string()}.csv"
    sessions = employee_report_export()
    with open(sessionDataCSV, "w+") as csv_output_file_pointer:
        csv_writer = csv.writer(csv_output_file_pointer)
        # Writing headers of CSV file
        header = (
            "SSN",
            "FirstName",
            "LastName",
            "MiddleName",
            "DateOfBirth",
            "Gender",
            "EmailAddress",
            "Ethnicity",
            "Race",
            "Qualifications",
            "LanguageCode",
            "ContractNumber",
            "EmployeeTitle",
            "TitleStartDate",
            "CaseLoad",
            "Prior to 10/01/2021",
            "TrainingDate",
            "InitialCBC",
            "MostCurrentCBC",
        )
        csv_writer.writerow(header)
        for employee in employees:
                row_data = (
                    employee["social_security"],
                    employee["first_name"],
                    employee["last_name"],
                    employee["middle_name"],
                    employee["max_score"],
                )
                csv_writer.writerow(row_data)
                os.open(sessionDataCSV, os.O_NONBLOCK)
    print("As You Wish mi'lord. One CSV Coming up")
