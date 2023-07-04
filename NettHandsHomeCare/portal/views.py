"""
Copyright (c) 2019 - present AppSeed.us
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic.detail import DetailView
from icecream import ic
from portal.forms import EmployeeForm
from portal.models import Employee
from django.shortcuts import render


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
#     return HttpResponse(render(request,'profile.html', context)
@login_required(login_url="/login/")
def profile_view(request):
    context = dict()
    context["data"] = Employee.objects.get(id=request.user.id)
    context["form"] = EmployeeForm
    return render(request, "home/profile.html", context)


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
def update_profile(request, id):
    user = Employee.objects.get(id=id)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/profile")
