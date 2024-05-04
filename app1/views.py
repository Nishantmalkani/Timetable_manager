import csv
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import *

from .models import *


@login_required(login_url='login')
def demo1(request):
    faculty_count = Facultydetail.objects.count()
    department_count = departments.objects.count()
    context = {
        'faculty_count': faculty_count,
        'department_count': department_count,
    }
    if 'user_login' in request.session:
        return render(request, 'index.html', context)
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
            raise ValueError(f"A subject with subject_code {subject_code} already exists.".format(subject_code))
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

    search_id = request.GET.get('search_id', '')
    search_name = request.GET.get('search_name', '')

    if search_id or search_name:
        dep = departments.objects.filter(Q(dept_id__iexact=search_id) & Q(dept_name__icontains=search_name))
    else:
        dep = departments.objects.all()

    entries_per_page = request.GET.get('entries', 10)  # Default to 10 entries per page
    paginator = Paginator(dep, entries_per_page)

    page_number = request.GET.get('page')
    dep1 = paginator.get_page(page_number)

    return render(request, 'department.html', {'dep': dep, 'dep1': dep1})


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
    search_code = request.GET.get('search_code', '')
    search_name = request.GET.get('search_name', '')
    sub = subjects.objects.filter(Q(subject_code__icontains=search_code) & Q(subject_name__icontains=search_name))
    # pagination
    # p = Paginator(subjects.objects, 10)
    # page = request.GET.get('page')
    # sub1 = p.get_page(page)
    entries_per_page = request.GET.get('entries', 10)  # Default to 10 entries per page
    paginator = Paginator(sub, entries_per_page)

    page_number = request.GET.get('page')
    sub1 = paginator.get_page(page_number)

    return render(request, 'subjects.html', {'sub': sub, 'sub1': sub1})


def teacherdetails(request, faculty_id):
    faculty = get_object_or_404(Facultydetail, faculty_id=faculty_id)
    return render(request, 'teacher-details.html', {'faculty': faculty})


def teacher(request):
    fac = Facultydetail.objects.all()
    search_id = request.GET.get('search_id', '')
    search_name = request.GET.get('search_name', '')
    sort_by = request.GET.get('sort_by', 'faculty_id')  # Default to sorting by faculty_id

    fac = Facultydetail.objects.filter(Q(faculty_id__icontains=search_id) & Q(faculty_name__icontains=search_name))
    entries_per_page = request.GET.get('entries', 10)  # Default to 10 entries per page
    paginator = Paginator(fac, entries_per_page)

    page_number = request.GET.get('page')
    fac1 = paginator.get_page(page_number)
    return render(request, 'teachers.html', {'fac': fac, 'fac1': fac1})


def timetable(request):
    time_tables = time_table_subject.objects.all()  
    time_table_field1 = time_table_field.objects.all()  
    search_name = request.GET.get('search_name', '')
    search_faculty = request.GET.get('search_faculty', '')
    search_semester = request.GET.get('search_semester', '')
    search_department = request.GET.get('search_department', '')

    time_tables = time_tables.filter(
        Q(subject__subject_name__icontains=search_name) |
        Q(faculty__faculty_name__icontains=search_faculty)
    )

    if search_semester.isdigit():
        time_tables = time_tables.filter(time_table__semester=search_semester)

    if search_department:
        time_tables = time_tables.filter(time_table__branch__name__icontains=search_department)

    return render(request, 'time-table.html', {'time_tables': time_tables, 'time_table_field1': time_table_field1})


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

def logout(request):
    if 'user_login' in request.session:
        del request.session['user_login']
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')



def forget_password(request):
    return render(request, 'forgot-password.html')


# def register(request):
#     return render(request, 'register.html')

def select_timetable(request):
    dept1 = departments.objects.all()
    subs = subjects.objects.all()
    facs = Facultydetail.objects.all()
    if request.method == 'POST':
        week_day = request.POST['week_day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        subject = request.POST['subjects']
        Faculty = request.POST['Faculty']
        print(week_day,start_time,end_time,subject,Faculty,"66666666666666")
        fieldobj = time_table_field.objects.last()
        subject_obj = subjects.objects.get(subject_name = subject)
        faculty_obj = Facultydetail.objects.get(faculty_name=Faculty)
        time_table_subject_obj = time_table_subject.objects.create(time_table=fieldobj, week_day=week_day,start_time=start_time,ends_time=end_time)
        time_table_subject_obj.subject.add(subject_obj)
        time_table_subject_obj.faculty.add(faculty_obj)
        return redirect('select_timetable')
        
    return render(request, 'add-time-table-subjects.html', {'dept1': dept1, 'subs': subs, 'facs': facs})


def add_timetable(request):
    dept1 = departments.objects.all()
    if request.method == 'POST':
    #     # Get the submitted data from the request
        branch = request.POST['branch']
        semester = request.POST['semester']
        class_section = request.POST['class']
        # print(branch,class_section,semester,"444444444444444")
        b1 = departments.objects.get(dept_name=branch)
        time_table_field.objects.create(branch=b1, division=class_section,semester=semester)
        return redirect('select_timetable')
    return render(request, 'add-time-table.html',{'dept1': dept1})


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


def download_faculty_details(request):
    faculty_details = Facultydetail.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="faculty_details.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Faculty ID', 'Faculty Name', 'Date of Birth', 'Department', 'Designation', 'Expertise', 'Qualification',
         'Join Date', 'Username', 'Phone', 'Address', 'City', 'State', 'Country', 'Zipcode', 'Email', 'Password'])

    for faculty in faculty_details:
        writer.writerow([faculty.faculty_id, faculty.faculty_name, faculty.date_of_birth, faculty.department.dept_name,
                         faculty.designation, faculty.expertise, faculty.qualification, faculty.join_date,
                         faculty.username, faculty.phone, faculty.address, faculty.city, faculty.state, faculty.country,
                         faculty.zipcode, faculty.email, faculty.password])

    return response


def download_subjects_details(request):
    subjects_details = subjects.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subjects_details.csv"'

    writer = csv.writer(response)
    writer.writerow(['Subject Code', 'Subject Name', 'Semester'])

    for subject in subjects_details:
        writer.writerow([subject.subject_code, subject.subject_name, subject.semester])

    return response


def download_department_details(request):
    department_details = departments.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="department_details.csv"'

    writer = csv.writer(response)
    writer.writerow(['Department ID', 'Department Name', 'HOD'])

    for department in department_details:
        writer.writerow([department.dept_id, department.dept_name, department.hod])

    return response


def delete_time_table(request, time_table_id):
    time_table = get_object_or_404(time_table_subject, id=time_table_id)
    time_table.delete()
    return redirect('/timetable/')


def edit_timetable(request, id1):
    subject = subjects.objects.all()
    faculty = Facultydetail.objects.all()
    timetable = time_table_subject.objects.all()
    timetable1 = get_object_or_404(time_table_subject, pk=id1)
    print("wwwwwwwwwwwwwwwwww")

    if request.method == 'POST':
        # Get the faculty and subject from the form data
        faculty_id = request.POST['faculty']
        subject_code = request.POST['subject']

        # Retrieve the faculty and subject instances from the database
        faculty = get_object_or_404(Facultydetail, id=faculty_id)
        subject = get_object_or_404(subject, id=subject_code)

        # Assign the faculty and subject to the timetable
        timetable1.faculty.set([faculty])
        timetable1.subject.set([subject])

        # Update other fields
        # Update other fields
        timetable1.semester = request.POST.get('semester')
        timetable1.division = request.POST.get('division')
        timetable1.week_day = request.POST.get('week_day')
        timetable1.start_time = request.POST.get('start_time')
        if 'start_time' in request.POST:
            timetable1.start_time = request.POST.get('start_time')
        else:
            # Assign a default value to timetable1.start_time
            timetable1.start_time = '08:00'

            timetable1.end_time = request.POST.get('end_time')
        timetable1.end_time = request.POST.get('end_time')

        # Save the changes
        timetable1.save()

        # Redirect to some page after the data is updated
        return redirect('/timetable/')

    # If the request is a GET request, display the current data
    return render(request, 'edit-time-table.html',
                  {'timetable1': timetable1, 'subject': subject, 'timetable': timetable, 'faculty': faculty})
