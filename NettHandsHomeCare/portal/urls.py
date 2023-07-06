from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    # The home page
    path("dashboard", views.index, name="home"),
    path("profile/", views.profile, name="profile"),
    # path("update-profile/", views.update_profile, name="change-profile")
    # Matches any html file
    # re_path(r"^.*\.*", views.pages, name="pages"),
]
