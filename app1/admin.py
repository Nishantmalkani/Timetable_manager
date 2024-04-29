from django.contrib import admin

from .models import *

# admin.site.register(department)
# admin.site.register(faculty)
# admin.site.register(subjects)
admin.site.register(vanue)


@admin.register(departments)
class departmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'dept_name', 'hod')

@admin.register(Facultydetail)
class FacultydetailAdmin(admin.ModelAdmin):
    list_display = (
        'faculty_id', 'faculty_name', 'date_of_birth', 'department', 'designation', 'expertise',
        'qualification', 'join_date', 'address', 'city', 'state', 'country', 'zipcode', 'username', 'phone', 'email',
        'password')

@admin.register(subjects)
class subjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code', 'subject_name', 'semester')


admin.site.register(timetable)

# @admin.register(timetable)
# class timetableInline(admin.ModelAdmin):
#     list_display = ('semester', 'subject', 'faculty', 'vanue', 'class_details', 'start_time', 'end_time', 'day')
