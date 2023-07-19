"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import admin
from employee.models import Employee
from compliance.models import Contract, Compliance
from portal.models import  Exception #Assessment, InServiceTraining,


# Register your models here.
all_models = [Employee, Contract, Exception, Compliance]

for model in all_models:
    register = admin.site.register(model)
