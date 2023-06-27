from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("client-interest/", views.client_interest, name="client-interest"),
    path("employment-application/", views.employee_interest, name="application"),
    path("submission-confirmation/", views.submitted, name="submitted"),
]
