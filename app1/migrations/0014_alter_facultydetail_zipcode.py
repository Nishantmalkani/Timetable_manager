# Generated by Django 5.0.3 on 2024-03-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0013_facultydetail_zipcode_alter_facultydetail_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facultydetail",
            name="zipcode",
            field=models.IntegerField(),
        ),
    ]
