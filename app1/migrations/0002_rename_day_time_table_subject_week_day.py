# Generated by Django 5.0.3 on 2024-04-30 05:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="time_table_subject",
            old_name="day",
            new_name="week_day",
        ),
    ]
