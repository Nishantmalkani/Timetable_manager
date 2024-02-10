from django.shortcuts import render

def demo1(request):
    return render(request,'index.html')

def adddepartment(request):
    return render(request, 'add-department.html')

def addsubject(request):
    return render(request, 'add-subject.html')

def addteacher(request):
    return render(request, 'add-teacher.html')

def department(request):
    return render(request, 'department.html')

def editdepartment(request):
    return render(request, 'edit-department.html')

def editsubject(request):
    return render(request,'edit-subject.html')

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
