"""
Copyright (c) 2019 - present AppSeed.us
"""
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


@login_required(login_url="/login/")
def index(request):
    context = {"segment": "index"}

    html_template = loader.get_template("home/index.html")
    return HttpResponse(html_template.render(context, request))


# class ProfileView(DetailView):
#     model = Employee
#     form_class = EmployeeForm
#     template_name = "home/profile.html"
#     success_url = "/profile"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# def get(request, pk):
#     context = dict()
#     context["form"] = EmployeeForm
# #     return HttpResponse(render(request,'profile.html', context)


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
        # except Exception:

        # else:
        #     context["form"] = EmployeeForm(initial=init_values)
        #     messages.error(request, form.errors)
        #     return render(request,'home/profile.html', context)
    elif request.method == "GET":
        context["form"] = EmployeeForm(initial=init_values)
        ic("GET Path")
        return render(
            request=request,
            template_name="home/profile.html",
            context=context,
        )

    # user = Employee.objects.get(id=request.user.id)
    # form = EmployeeForm(request.POST)
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return redirect("/profile")
    #     else:
    #         return redirect()
