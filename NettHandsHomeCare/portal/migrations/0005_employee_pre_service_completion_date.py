# Generated by Django 4.2.2 on 2023-07-03 10:02
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0004_employee_job_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="pre_service_completion_date",
            field=models.DateField(null=True),
        ),
    ]
