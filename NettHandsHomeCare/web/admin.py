from django.contrib import admin
from web.models import ClientInterestSubmissions
from web.models import EmploymentApplicationModel

# Register your models here.
all_models = [ClientInterestSubmissions, EmploymentApplicationModel]

for model in all_models:
    register = admin.site.register(model)
