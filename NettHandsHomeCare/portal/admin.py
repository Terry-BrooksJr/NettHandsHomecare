from django.contrib import admin
from portal.models import Assessment
from portal.models import Employee

# Register your models here.
all_models = [Assessment, Employee]

for model in all_models:
    register = admin.site.register(model)
