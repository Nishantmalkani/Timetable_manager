# Generated by Django 5.0.3 on 2024-03-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0014_alter_facultydetail_zipcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facultydetail",
            name="city",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="facultydetail",
            name="country",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="facultydetail",
            name="state",
            field=models.CharField(max_length=500),
        ),
    ]