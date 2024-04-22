from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
import json
from usermodule.models import CustomUser,Student,Staff, Semester, HOD, Courses
from datamodule.models import Attendance, AttendanceReport, Session, Subject, SubjectWithStaff

# Create your views here.

usertypedata = {1:"HOD", 2:"Staff",3:"Student"}
SEMdata = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
YEARdata = ["1st", "1st", "2nd", "2nd", "3rd", "3rd"]
DEPTdata = ["CST", "EE", "ME", "ETC"]



@login_required(login_url="/login")
def index(request):
    user = request.user
    if int(user.user_type) == 1:
       return redirect("hodDashboard")
    elif int(user.user_type) == 2:       
        return redirect("staffDashboard")
    elif int(user.user_type) == 3:
        return redirect("studentDashboard")


@login_required(login_url="/login")
def ThankYou(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        User = Student.objects.filter(student=user).first()
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)]
    }
    return render(request, "ThankYou.html", data)


@login_required(login_url="/login")
def Student_list(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        User = Student.objects.filter(student=user).first()
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)]
    }
    data["studentTable"] =  Student.objects.all()
    return render(request, "student.html", data) 


@login_required(login_url="/login")
def Staff_list(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        User = Student.objects.filter(student=user).first()
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)]
    }
    data["staffTable"] =  Staff.objects.all()
    return render(request, "staff.html", data) 


@login_required(login_url="/login")
def HOD_list(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        User = Student.objects.filter(student=user).first()
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)]
    }
    data["HODTable"] =  HOD.objects.all()
    return render(request, "hod.html", data) 


@login_required(login_url="/login")
def HOD_Dashboard(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        return redirect("staffDashboard")
    elif int(user.user_type) == 3:
        return redirect("studentDashboard")
    data = {
        "user": User, 
        "usertype": usertypedata[int(user.user_type)],
        "studentNo": Student.objects.count(),
        "studentMale": Student.objects.filter(gender="Male").count(),
        "studentFemale": Student.objects.filter(gender="Female").count(),
        "staffNo": Staff.objects.count(),
        "courseNo": Courses.objects.count(),
        "subjectNo": Subject.objects.count(),
        "courses": {(course.course_name, json.dumps([random.randint(40, 100) for _ in range(12)])) for course in Courses.objects.all()},
    }
    return render(request, "hodDashboard.html", data) 


@login_required(login_url="/login")
def Student_Dashboard(request):
    user = request.user
    if int(user.user_type) == 1:
        return redirect("hodDashboard")
    elif int(user.user_type) == 2:
        return redirect("staffDashboard")
    elif int(user.user_type) == 3:
        student = Student.objects.filter(student=user).first()
    data = {
        "user": student,
        "Sem": SEMdata, "Dept": DEPTdata,
        "photo": student.photo.url if student else "",
        "RegID": student.reg_id if student else "",
        "Name": student.name if student else "",
        "DOB": student.dob if student else "",
        "Gender": student.gender if student else "Male",
        "Phone": student.phone if student else "",
        "Email": student.email if student else "",
        "semester": student.sem.semester if student else "1st",
        "department": student.course_id.course_name if student else "CST",
        "usertype": usertypedata[int(user.user_type)],
        "studentNo": Student.objects.count(),
        "studentMale": Student.objects.filter(gender="Male").count(),
        "studentFemale": Student.objects.filter(gender="Female").count(),
        "staffNo": Staff.objects.count(),
        "courseNo": Courses.objects.count(),
        "subjectNo": Subject.objects.count(),
    }
    return render(request, "studentDashboard.html", data) 


@login_required(login_url="/login")
def Staff_Dashboard(request):
    user = request.user
    if int(user.user_type) == 1:
        return redirect("hodDashboard")
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        return redirect("studentDashboard")
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)],
        "studentNo": Student.objects.count(),
        "studentMale": Student.objects.filter(gender="Male").count(),
        "studentFemale": Student.objects.filter(gender="Female").count(),
        "staffNo": Staff.objects.count(),
        "courseNo": Courses.objects.count(),
        "subjectNo": Subject.objects.count(),
    }
    return render(request, "staffDashboard.html", data) 


@login_required(login_url="/login")
def Student_Edit(request):
    user = request.user
    if int(user.user_type) != 3:
        return redirect("index")
    else:
        student = Student.objects.filter(student=user).first()
        if request.method == "POST":

            form_data = request.POST
            form_files = request.FILES

            sem = Semester.objects.get(semester=form_data["CurrentSemester"])
            dep = Courses.objects.get(course_name=form_data["Major"])

            photo = form_files.get("Photo")
            student.photo =photo if photo else student.photo
            student.reg_id = form_data["regid"]
            student.name = form_data["Name"]
            student.dob = form_data["Birthday"]
            student.gender = form_data["Gender"]
            student.course_id = dep
            student.sem = sem
            student.phone = form_data["PhoneNumber"]
            student.email = form_data["Email"]
            student.save()
            messages.success(request, "Profile Updated successfully")
            return redirect("index")
        
        else:

            data = {
                "user": student,
                "usertype": usertypedata[int(user.user_type)],
                "Sem": SEMdata, "Dept": DEPTdata,
                "photo": student.photo.url,
                "RegID": student.reg_id ,
                "Name": student.name ,
                "DOB": student.dob ,
                "Gender": student.gender ,
                "Phone": student.phone ,
                "Email": student.email ,
                "semester": student.sem.semester ,
                "department": student.course_id.course_name ,
            }   
        return render(request, "studentEdit.html", data)


@login_required(login_url="/login")
def Staff_Edit(request):
    user = request.user
    if int(user.user_type) != 2:
        return redirect("index")
    else:
        staff = Staff.objects.filter(staff=user).first()
        if request.method == "POST":

            form_data = request.POST
            form_files = request.FILES

            photo = form_files.get("Photo")
            staff.photo =photo if photo else staff.photo
            staff.name = form_data["Name"]
            staff.dob = form_data["Birthday"]
            staff.gender = form_data["Gender"]
            staff.phone = form_data["PhoneNumber"]
            staff.email = form_data["Email"]
            staff.save()
            messages.success(request, "Profile Updated successfully")
            return redirect("index")
        
        else:

            data = {
                "user": staff,
                "usertype": usertypedata[int(user.user_type)],
                "photo": staff.photo.url,
                "Name": staff.name ,
                "DOB": staff.dob ,
                "Gender": staff.gender ,
                "Phone": staff.phone ,
                "Email": staff.email ,
            }   
        return render(request, "staffEdit.html", data)


@login_required(login_url="/login")
def HOD_Edit(request):
    user = request.user
    if int(user.user_type) != 1:
        return redirect("index")
    else:
        hod = HOD.objects.filter(hod=user).first()

        if request.method == "POST":

            form_data = request.POST
            hod.name = form_data["Name"]
            hod.email = form_data["Email"]
            hod.save()
            messages.success(request, "Profile Updated successfully")
            return redirect("index")
        
        else:

            data = {
                "user": hod,
                "usertype": usertypedata[int(user.user_type)],
                "Name": hod.name,
                "Email": hod.email,
            }   
        return render(request, "hodEdit.html", data)
                

@login_required(login_url="/login")
def add_course(request):
    user = request.user
    if int(user.user_type) != 1:
        return redirect("index")
    else:
        hod = HOD.objects.filter(hod=user).first()
    if request.method == 'POST':
        name = request.POST.get('Name')
        try:
            Courses.objects.create(course_name=name).save()
            messages.success(request, "Course Successfully Added")
            return redirect('index')
        except:
            pass
        messages.error(request, "Course Adding Unsuccessful")
    else:
        pass
    data = {
            "user": hod,
            "usertype": usertypedata[int(user.user_type)],
    }  
    return render(request, 'courseNew.html', data)  
                

@login_required(login_url="/login")
def Course_list(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        User = Student.objects.filter(student=user).first()
    courses = Courses.objects.all()

    # Prepare courseTable data
    courseTable = []
    for course in courses:
        course_data = {
            'course_name': course.course_name,
            'subjects': {}
        }

        # Group subjects by semester
        subjects = SubjectWithStaff.objects.filter(subject_id=Subject.objects.filter(course_id=course).first())
        for subject in subjects:
            semester = subject.subject_id.semester_id.semester  # Assuming subjects have a 'semester' field

            if semester in course_data['subjects']:

                course_data['subjects'][semester].append(subject.subject_id.subject_name)

            else:

                course_data['subjects'][semester] = [subject.subject_id.subject_name]

        courseTable.append(course_data)
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)],
        "courseTable": courseTable,
    }  
    return render(request, 'course.html', data)  


@login_required(login_url="/login")
def add_subject(request):
    user = request.user
    if int(user.user_type) != 1:
        return redirect("index")
    else:
        hod = HOD.objects.filter(hod=user).first()

    if request.method == 'POST':
        name = request.POST.get('Name')
        course = Courses.objects.filter(course_name=request.POST.get('Major')).first()
        sem = Semester.objects.filter(semester=request.POST.get('Semester')).first()
        
        if Subject.objects.filter(subject_name=name, course_id=course, semester_id=sem).exists():
            messages.error(request, "Subject Name Already Exists!")
        else:
            try:
                Subject.objects.create(subject_name=name, course_id=course, semester_id=sem)
                messages.success(request, "Subject Successfully Added")
                return redirect('index')
            except Exception as e:
                messages.error(request, "Subject Adding Unsuccessful: {}".format(str(e)))

    data = {
        "user": hod,
        "usertype": usertypedata[int(user.user_type)],
        "Sem": SEMdata,
        "Dept": DEPTdata,
    }
    
    return render(request, 'subjectNew.html', data)


@login_required(login_url="/login")
def Subject_list(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        User = Student.objects.filter(student=user).first()

    subjects = Subject.objects.all()

    # Prepare courseTable data
    subjectTable = []
    for subject in subjects:
        subject_data = {
            'subject_name': subject.subject_name,
            'course_name': subject.course_id.course_name,
            'semester_name': subject.semester_id.semester,
        }
        subjectTable.append(subject_data)
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)],
        "subjectTable": subjectTable,
    }  
    return render(request, 'subject.html', data)  


@login_required(login_url="/login")
def SubjectForTeacher(request):
    user = request.user
    if int(user.user_type) != 1:
        return redirect("index")
    else:
        hod = HOD.objects.filter(hod=user).first()

    if request.method == 'POST':
        name = request.POST.get('Name')
        course = Courses.objects.filter(course_name=request.POST.get('Major')).first()
        sem = Semester.objects.filter(semester=request.POST.get('Semester')).first()
        
        if Subject.objects.filter(subject_name=name, course_id=course, semester_id=sem).exists():
            messages.error(request, "Subject Name Already Exists!")
        else:
            try:
                Subject.objects.create(subject_name=name, course_id=course, semester_id=sem)
                messages.success(request, "Subject Successfully Added")
                return redirect('index')
            except Exception as e:
                messages.error(request, "Subject Adding Unsuccessful: {}".format(str(e)))

    data = {
        "user": hod,
        "usertype": usertypedata[int(user.user_type)],
        "Subject": Subject.objects.all(),
        "Staff": Staff.objects.all(),
        "Session": Session.objects.all(),
    }
    
    return render(request, 'subjectNew.html', data)


@login_required(login_url="/login")
def add_session(request):
    user = request.user
    if int(user.user_type) != 1:
        return redirect("index")
    else:
        hod = HOD.objects.filter(hod=user).first()

    if request.method == 'POST':
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        if not Session.objects.filter(session_start_year=session_start_year, session_end_year=session_end_year).exists():

        # Create a new Session object
            try:
                Session.objects.create(
                    session_start_year=session_start_year,
                    session_end_year=session_end_year
                ).save()
                messages.success(request, "Session Adding Successful")
                return redirect('index')
            except Exception as e:
                messages.error(request, "Session Adding Unsuccessful: {}".format(str(e)))

        else:
            messages.error(request, "Session Already Exist ! ")
    data = {
        "user": hod,
        "usertype": usertypedata[int(user.user_type)],
    }
    
    return render(request, 'session.html', data)


@login_required(login_url="/login")
def Session_list(request):
    user = request.user
    if int(user.user_type) == 1:
        User = HOD.objects.filter(hod=user).first()
    elif int(user.user_type) == 2:
        User = Staff.objects.filter(staff=user).first()
    elif int(user.user_type) == 3:
        User = Student.objects.filter(student=user).first()

    sessions = Session.objects.all()

    # Prepare courseTable data
    sessionTable = []
    for n,session in enumerate(sessions):
        session_data = (n+1, str(session.session_start_year.year)+'-'+str(session.session_end_year.year))
        sessionTable.append(session_data)
    data = {
        "user": User,
        "usertype": usertypedata[int(user.user_type)],
        "sessionTable": sessionTable,
    }  
    return render(request, 'sessionlist.html', data)  

