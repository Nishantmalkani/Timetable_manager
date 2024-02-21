from django.contrib import admin

from .models import *

# admin.site.register(department)
# admin.site.register(faculty)
admin.site.register(subject)
admin.site.register(vanue)


@admin.register(department)
class departmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'dept_name', 'hod')


@admin.register(faculty)
class facultyAdmin(admin.ModelAdmin):
    list_display = (
        'faculty_id', 'name', 'date_of_birth', 'department', 'designation', 'expertise', 'qualification', 'join_date',
        'address', 'phone', 'email', 'password')
