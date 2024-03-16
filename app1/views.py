import random

from django.shortcuts import *

from .models import *


def demo1(request):
    return render(request, 'index.html')


def adddepartment(request):
    if request.method == 'POST':
        dept_id = request.POST['dept_id']
        dept_name = request.POST['dept_name']
        hod = request.POST['hod']
        departments(dept_id=dept_id, dept_name=dept_name, hod=hod).save()
    return render(request, 'add-department.html')


def addsubject(request):
    if request.method == 'POST':
        subject_code = request.POST['subject_code']
        subject_name = request.POST['subject_name']
        semester = request.POST['semester']
        # print(subject_code,subject_name,semester,"ssssssssssssssssssss")
        subjects(subject_name=subject_name, subject_code=subject_code, semester=semester).save()
    return render(request, 'add-subject.html')


def addteacher(request):
    dept = departments.objects.all()
    ran = random.randint(1111, 9999)
    if request.method == 'POST':
        faculty_id = ran
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        # gender = request.POST.get('gender')
        department = request.POST['department']
        for i in dept:
            if department == i.dept_name:
                d = departments.objects.get(pk=i.id)
                # print(d,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

        designation = request.POST['designation']
        expertise = request.POST['expertise']
        qualification = request.POST['qualification']
        join_date = request.POST['join_date']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        print(faculty_id, name, date_of_birth, department, designation, expertise, qualification, join_date, phone,
              address, email, password)
        Facultydetail(faculty_id=faculty_id, faculty_name=name, date_of_birth=date_of_birth, department=d,
                      designation=designation, expertise=expertise, qualification=qualification, join_date=join_date,
                      phone=phone, address=address, email=email, password=password).save()
        return render(request, 'add-teacher.html', {'dept': dept})
    else:
        return render(request, 'add-teacher.html', {'dept': dept})


def department(request):
    dep = departments.objects.all()
    return render(request, 'department.html', {'dep': dep})


def editdepartment(request):
    return render(request, 'edit-department.html')


def editsubject(request):
    return render(request, 'edit-subject.html')


def editteacher(request):
    return render(request, 'edit-teacher.html')


def subject(request):
    sub = subjects.objects.all()
    return render(request, 'subjects.html', {'sub': sub})


def teacherdetails(request):
    return render(request, 'teacher-details.html')


def teacher(request):
    fac = Facultydetail.objects.all()
    return render(request, 'teachers.html', {'fac': fac})


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


def delete_data(request, id):
    if request.method == 'POST':
        pi = Facultydetail.objects.get(pk=id)
        pi.delete()
    return redirect('/teacher/')


def delete_department(request, id1):
    if request.method == 'POST':
        pi = departments.objects.get(pk=id1)
        pi.delete()
    return redirect('/department/')


def delete_subject(request, id2):
    if request.method == 'POST':
        pi = subjects.objects.get(pk=id2)
        pi.delete()
    return redirect('/subject/')
