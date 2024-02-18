from django.shortcuts import render

from .models import *


def demo1(request):
    return render(request, 'index.html')


def adddepartment(request):
    return render(request, 'add-department.html')


def addsubject(request):
    return render(request, 'add-subject.html')


def addteacher(request):
    if request.method == 'POST':
        faculty_id = request.POST['faculty_id']
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        departments = request.POST['department']
        designation = request.POST['designation']
        expertise = request.POST['expertise']
        qualification = request.POST['qualification']
        join_date = request.POST['join_date']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        faculty(faculty_id=faculty_id, name=name, date_of_birth=date_of_birth, department=departments,
                designation=designation, expertise=expertise, qualification=qualification, join_date=join_date,
                phone=phone, address=address, email=email, password=password).save()
    return render(request, 'add-teacher.html')


def department(request):
    return render(request, 'department.html')


def editdepartment(request):
    return render(request, 'edit-department.html')


def editsubject(request):
    return render(request, 'edit-subject.html')


def editteacher(request):
    return render(request, 'edit-teacher.html')


def subject(request):
    return render(request, 'subjects.html')


def teacherdetails(request):
    return render(request, 'teacher-details.html')


def teacher(request):
    return render(request, 'teachers.html')


def timetable(request):
    return render(request, 'time-table.html')


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


def edit_timetable(request):
    return render(request, 'edit-time-table.html')


def forget_password(request):
    return render(request, 'forgot-password.html')


def register(request):
    return render(request, 'register.html')


def add_timetable(request):
    return render(request, 'add-time-table.html')
