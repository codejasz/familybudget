# Generated by Django 4.1 on 2023-01-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("familybudgetapp", "0002_alter_budget_expenses_alter_budget_incomes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="budget",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="budget",
            name="name",
            field=models.CharField(default="default", max_length=30),
            preserve_default=False,
        ),
    ]