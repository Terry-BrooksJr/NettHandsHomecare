"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from portal.models import Employee

# Register your models here.
all_models = [Employee]

for model in all_models:
    register = admin.site.register(model)
