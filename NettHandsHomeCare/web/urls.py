from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("client-interest/", views.client_interest, name="client-interest"),
    path("submission-confirmation/", views.submitted, name="submitted"),
]
