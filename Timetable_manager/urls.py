"""Timetable_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app1 import views
from app1.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.demo1, name='index'),
    path("add-department/", views.adddepartment, name='add-department'),
    path("add-subject/", views.addsubject, name='add-subject'),
    path("add-teacher/", views.addteacher, name='add-teacher'),
    path("editsubject/<int:subject_code>", views.editsubject, name='editsubject'),
    path("department/", views.department, name='department'),
    path("edit-department/<int:dept_id>", views.editdepartment, name='edit-department'),
    path("edit-teacher/", views.editteacher, name='edit-teacher'),
    path("subject/", views.subject, name='subject'),
    path("teacher-details/", views.teacherdetails, name='teacher-details'),
    path("teacher/", views.teacher, name='teacher'),
    path("timetable/", views.timetable,name='timetable'),
    path("login/", views.login, name='login'),
    path("profile/", views.profile, name='profile'),
    path("edit-time-tabel/", views.edit_timetable, name="edit-time-tabel"),
    path("forget-password/", views.forget_password, name="forget-password"),
    path("register/", views.register, name="register"),
    path("add-time-table/", views.add_timetable, name="add-time-table"),
    path("subject/<int:faculty_id>/", views.delete_data, name="delete_data"),
    path("department/<int:dept_id>/", views.delete_department, name="delete_department"),
    path("subject/<int:subject_code>/", views.delete_subjects, name="delete_subjects"),
]


