from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import reverse
from django.template import loader
from django.urls import reverse
from django.views.generic.detail import DetailView
from icecream import ic
from portal.forms import EmployeeForm
from portal.models import Employee
from web.forms import ClientInterestForm
from web.models import ClientInterestSubmissions
import json
import os
from django.core.serializers.json import DjangoJSONEncoder

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
    }

    if request.method == "POST":
        ic("POST Path")
        user = Employee.objects.get(username=request.user.username)
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        ic(form.data.get("social_security"))

        # check whether it's valid:
        # if form.has_error("social_security","username"):
        #     if form.is_valid():
        # try:
        user.social_security = form.data.get("social_security")
        user.street_address = form.data.get("street_address")
        user.phone = form.data.get("phone")
        user.zipcode = form.data.get("zipcode")
        user.middle_name = form.data.get("middle_name")
        user.emergency_contact_relationship = form.data.get(
            "emergency_contact_relationship",
        )
        user.email = form.data.get("email")
        user.emergency_contact_first_name = form.data.get(
            "emergency_contact_first_name",
        )
        user.emergency_contact_last_name = form.data.get("emergency_contact_last_name")
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
        ic("GET Path")
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
    context["reviewed"] = ClientInterestSubmissions.objects.filter(reviewed=True).count()
    context["all_submuission"] =  ClientInterestSubmissions.objects.all().count
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
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        pk = body['pk']
        submission = ClientInterestSubmissions.objects.get(id=pk)
        submission.marked_reviewed(request.user)
        submission.save()
        return HttpResponse(status=204)
    except Exception as e:
        ic(e)
        return HttpResponse(status=418)

