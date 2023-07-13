from django.urls import path
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("dashboard", views.index, name="home"),
    path("my-profile/", views.profile, name="profile"),
    path("inquiries/", views.client_inquiries, name="inquiries"),
    path(
        "inquiries/<int:pk>/",
        views.submission_detail,
        name="client_interest_details",
    ),
    path("employee-details/<int:pk>", views.employee_details, name="roster-profile"),
    path(
        "reviewed",
        csrf_exempt(views.marked_reviewed),
        name="marked_reviewed",
    ),
    path(
        "all_client_inquiries/",
        csrf_exempt(views.all_client_inquiries),
        name="all_client_inquiries",
    ),
    path("hired", csrf_exempt(views.hire), name="hire-applicant"),
    path("applicants/", views.employment_applications, name="applicants-list"),
    path("rejected", csrf_exempt(views.reject), name="reject-application"),
    path("applicant/<int:pk>", views.applicant_details, name="applicant-details"),
    path("all_applicants", views.all_applicants, name="submitted-applicants-api"),
    path("roster/", views.employee_roster, name="roster"),
    path("all-employees/", views.employee_report_export, name="employee-export"),
    # Matches any html file
    # re_path(r"^.*\.*", views.pages, name="pages"),
]
