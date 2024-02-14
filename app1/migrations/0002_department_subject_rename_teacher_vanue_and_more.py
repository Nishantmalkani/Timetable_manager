# Generated by Django 5.0.1 on 2024-02-14 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="department",
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
                ("dept_name", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="subject",
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
                ("subject_name", models.CharField(max_length=500)),
                ("subject_code", models.CharField(max_length=500)),
                ("semester", models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name="Teacher",
            new_name="vanue",
        ),
        migrations.RenameField(
            model_name="vanue",
            old_name="name",
            new_name="vanue_name",
        ),
        migrations.CreateModel(
            name="faculty",
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
                ("name", models.CharField(max_length=500)),
                ("faculty_id", models.CharField(max_length=500)),
                ("date_of_birth", models.DateField()),
                ("designation", models.CharField(max_length=500)),
                ("qualification", models.CharField(max_length=500)),
                ("expertise", models.CharField(max_length=500)),
                ("join_date", models.DateField()),
                ("phone", models.CharField(max_length=500)),
                ("address", models.CharField(max_length=500)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=500)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.department",
                    ),
                ),
            ],
        ),
    ]
