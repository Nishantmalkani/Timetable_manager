from django.db import models


class department(models.Model):
    dept_id = models.CharField(max_length=500)
    dept_name = models.CharField(max_length=500)
    hod = models.CharField(max_length=500)


class faculty(models.Model):
    faculty_id = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    # gender = models.CharField(max_length=500)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=500)
    expertise = models.CharField(max_length=500)
    qualification = models.CharField(max_length=500)
    join_date = models.DateField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField()
    password = models.CharField(max_length=500)


class subject(models.Model):
    subject_name = models.CharField(max_length=500)
    subject_code = models.CharField(max_length=500)
    semester = models.IntegerField()


class vanue(models.Model):
    vanue_name = models.CharField(max_length=500)
