from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import *

from .models import *


@login_required(login_url='login')
def demo1(request):
    if 'user_login' in request.session:
        return render(request, 'index.html')
    else:
        return redirect('login')


def adddepartment(request):
    if 'user_login' in request.session:
        if request.method == 'POST':
            dept_id = request.POST['dept_id']
            dept_name = request.POST['dept_name']
            hod = request.POST['hod']

            if departments.objects.filter(dept_id=dept_id).exists():
                raise ValueError(f"A department with dept_id {dept_id} already exists.")
            else:
                department = departments(dept_id=dept_id, dept_name=dept_name, hod=hod)
                department.save()
                return redirect('/department/')

        return render(request, 'add-department.html')
    else:
        return redirect('login')


def addsubject(request):
    if request.method == 'POST':
        subject_code = request.POST['subject_code']
        subject_name = request.POST['subject_name']
        semester = request.POST['semester']

        if subjects.objects.filter(subject_code=subject_code).exists():
            raise ValueError(f"A subject with subject_code {subject_code} already exists.")
        else:
            subjects(subject_name=subject_name, subject_code=subject_code, semester=semester).save()
            return redirect('/subject/')
        # print(subject_code,subject_name,semester,"ssssssssssssssssssss")

    return render(request, 'add-subject.html')


def addteacher(request):
    dept = departments.objects.all()
    # ran = random.randint(1111, 9999)
    if request.method == 'POST':
        faculty_id = request.POST['faculty_id']
        name = request.POST['name']
        date_of_birth_string = request.POST['date_of_birth']
        date_of_birth = datetime.strptime(date_of_birth_string, '%Y-%m-%d').date()
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
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zipcode = request.POST['zipcode']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        if Facultydetail.objects.filter(faculty_id=faculty_id).exists():
            raise ValueError(f"A teacher with faculty_id {faculty_id} already exists.")
        else:

            print(faculty_id, name, date_of_birth, department, designation, expertise, qualification, join_date,
                  username, phone,
                  address, city, state, country, zipcode, username, email, password)
            Facultydetail.objects.create(
                faculty_id=faculty_id,
                faculty_name=name,
                date_of_birth=date_of_birth,
                department=d,
                designation=designation,
                expertise=expertise,
                qualification=qualification,
                join_date=join_date,
                username=username,
                phone=phone,
                address=address,
                city=city,
                state=state,
                country=country,
                zipcode=zipcode,
                email=email,
                password=password
            )
            return redirect('/teacher/')

    return render(request, 'add-teacher.html', {'dept': dept})


def department(request):
    dep = departments.objects.all()
    return render(request, 'department.html', {'dep': dep})


def editdepartment(request, dept_id):
    depart = departments.objects.get(dept_id=dept_id)
    if request.method == 'POST':
        depart.dept_id = request.POST['dept_id']
        depart.dept_name = request.POST['dept_name']
        depart.hod = request.POST['hod']
        depart.save()
        return redirect('/department/')
    return render(request, 'edit-department.html', {'depart': depart})


def editsubject(request, subject_code):
    sub = subjects.objects.get(subject_code=subject_code)
    # print(sub,"jjjjjjjjjjjjjjjjjjjjjjj")
    if request.method == "POST":
        sub.subject_name = request.POST["subject_name"]
        sub.subject_code = request.POST["subject_code"]
        sub.semester = request.POST["semester"]
        sub.save()
        return redirect('/subject/')
    return render(request, 'edit-subject.html', {'sub': sub})


def editteacher(request, faculty_id):
    tch = Facultydetail.objects.get(faculty_id=faculty_id)
    deps = departments.objects.get(dept_id=tch.department.dept_id)
    deps1 = departments.objects.all()
    if request.method == "POST":
        tch.faculty_id = request.POST['faculty_id']
        tch.faculty_name = request.POST['faculty_name']

        date_of_birth_string = request.POST['date_of_birth']
        date_of_birth = datetime.strptime(date_of_birth_string, '%Y-%m-%d').date()
        tch.date_of_birth = date_of_birth

        department_name = request.POST.get('department')
        for i in deps1:
            if department == i.dept_name:
                d = departments.objects.get(pk=i.id)

        tch.designation = request.POST['designation']
        tch.expertise = request.POST['expertise']
        tch.qualification = request.POST['qualification']

        join_date_string = request.POST['join_date']
        join_date = datetime.strptime(join_date_string, '%Y-%m-%d').date()
        tch.join_date = join_date

        tch.phone = request.POST['phone']
        tch.address = request.POST['address']
        tch.city = request.POST['city']
        tch.state = request.POST['state']
        tch.country = request.POST['country']
        tch.zipcode = request.POST['zipcode']
        tch.username = request.POST['username']
        tch.email = request.POST['email']
        tch.password = request.POST['password']
        tch.save()
        return redirect('/teacher/')
    return render(request, 'edit-teacher.html', {'tch': tch, 'deps': deps})

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


# @login_required(login_url='dashboard')
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user_info = Facultydetail.objects.get(email=email)
            if user_info.password == password:
                request.session['user_login'] = email
                user = request.session['user_login']
                return redirect('dashboard')
        except:
            return render(request, 'login')
    else:

        return render(request, 'login.html')


# def _is_faculty_user(user):
#     try:
#         Facultydetail.objects.get(user=user)
#         return True
#     except Facultydetail.DoesNotExist:
#         return False


def logout(request):
    if 'user_login' in request.session:
        del request.session['user_login']
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')


def edit_timetable(request):
    return render(request, 'edit-time-table.html')


def forget_password(request):
    return render(request, 'forgot-password.html')


# def register(request):
#     return render(request, 'register.html')


def add_timetable(request):
    dept1 = departments.objects.all()
    for i in dept1:
        if department == i.dept_name:
            d1 = departments.objects.get(pk=i.id)

    return render(request, 'add-time-table.html', {'dept1': dept1})


def delete_data(request, faculty_id):
    # pi = None
    pi = get_object_or_404(Facultydetail, faculty_id=faculty_id)
    if request.method == 'POST':
        pi.delete()
    return redirect('/teacher/', {'pi': pi})


def delete_department(request, dept_id):
    # pi1 = None
    pi1 = get_object_or_404(departments, dept_id=dept_id)
    if request.method == 'POST':
        pi1.delete()
    return redirect('/department/')  # Remove unnecessary arguments


def delete_subjects(request, subject_code):
    pi2 = get_object_or_404(subjects, subject_code=subject_code)
    if request.method == 'POST':
        pi2.delete()
    return redirect('/subject/')  # Remove unnecessary arguments

