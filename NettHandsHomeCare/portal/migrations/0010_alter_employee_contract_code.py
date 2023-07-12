# Generated by Django 4.2.2 on 2023-07-12 13:02
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("portal", "0009_contract_employee_contract_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="contract_code",
            field=models.ForeignKey(
                blank=True,
                choices=[],
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="portal.contract",
            ),
        ),
    ]
