from django.db import models


class departments(models.Model):
    dept_id = models.CharField(max_length=500, unique=True)
    dept_name = models.CharField(max_length=500)
    hod = models.CharField(max_length=500)


# class faculty(models.Model):
#     faculty_id = models.CharField(max_length=500)
#     name = models.CharField(max_length=500)
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=500)
#     department = models.ForeignKey(departments, on_delete=models.CASCADE)
#     designation = models.CharField(max_length=500)
#     expertise = models.CharField(max_length=500)
#     qualification = models.CharField(max_length=500)
#     join_date = models.DateField()
#     address = models.CharField(max_length=500)
#     phone = models.CharField(max_length=500)
#     email = models.EmailField()
#     password = models.CharField(max_length=500)

class Facultydetail(models.Model):
    faculty_id = models.CharField(max_length=30, unique=True)
    faculty_name = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    # gender = models.CharField(max_length=500)
    department = models.ForeignKey(departments, on_delete=models.CASCADE)
    designation = models.CharField(max_length=500)
    expertise = models.CharField(max_length=500)
    qualification = models.CharField(max_length=500)
    join_date = models.DateField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    zipcode = models.IntegerField(unique=True)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)
    def __str__(self):
        return self.faculty_name
    

class subjects(models.Model):
    subject_code = models.CharField(max_length=500, unique=True)
    subject_name = models.CharField(max_length=500)
    semester = models.IntegerField()
    def __str__(self):
        return self.subject_name


class vanue(models.Model):
    vanue_name = models.CharField(max_length=500)

class time_table_field(models.Model):
    branch = models.ForeignKey(departments,on_delete=models.CASCADE)
    semester = models.IntegerField()
    division = models.CharField(max_length=500)
    def __str__(self):
        return self.division
    
    

class time_table_subject(models.Model):
    time_table = models.ForeignKey(time_table_field,on_delete=models.CASCADE)
    subject = models.ManyToManyField(subjects)
    faculty = models.ManyToManyField(Facultydetail)
    week_day = models.CharField(max_length=500)
    start_time = models.TimeField()
    ends_time = models.TimeField()



