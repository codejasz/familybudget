# Generated by Django 4.1 on 2023-01-24 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("familybudgetapp", "0008_alter_shared_budget_alter_transaction_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shared",
            name="budget",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="familybudgetapp.budget"
            ),
        ),
    ]