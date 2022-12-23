# Generated by Django 4.1.4 on 2022-12-23 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("UserProfil", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Broker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("broker_name", models.CharField(max_length=20)),
                ("broker_user_name", models.CharField(max_length=20)),
                ("broker_password", models.CharField(max_length=20)),
                ("broker_account_date", models.CharField(max_length=20)),
                ("broker_account_number", models.CharField(max_length=20)),
                ("broker_starting_balance", models.CharField(max_length=20)),
                ("broker_profit_loss", models.CharField(max_length=20)),
                (
                    "broker_user_id",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="UserProfil.user",
                    ),
                ),
            ],
        ),
    ]
