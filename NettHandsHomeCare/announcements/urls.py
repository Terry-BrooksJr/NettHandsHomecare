from django.urls import path
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
        path("announcements", views.announcements, name="announcements"),
        path(
        "create-announcement-draft",
        views.save_announcement,
        name="create-announcement",
    ),
]