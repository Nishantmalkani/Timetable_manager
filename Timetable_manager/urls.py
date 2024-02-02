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
from app1 import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.demo1,name='index'),
    path("add-department/", views.adddepartment,name='add-department'),
    path("add-subject/", views.addsubject,name='add-subject'),
    path("add-teacher/", views.addteacher),
    path("editsubject/", views.editsubject,name='editsubject'),
    path("department/", views.department,name='department'),
    path("edit-department/", views.editdepartment,name='edit-department'),
    path("edit-teacher/", views.editteacher),
    path("subject/", views.subject,name='subject'),
    path("teacher-details/", views.teacherdetails),
    path("teacher/", views.teacher),
    path("timetable/", views.timetable,name='timetable'),
    path("login/", views.login),
]


