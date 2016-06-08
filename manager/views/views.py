from django.shortcuts import render
from registration.models import Course, Student,Teacher
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout

from manager.forms import CourseForm, StudentForm,TeacherForm,ChangePasswordForm, SearchForm
from django.db.models import Q


def index(request):
    return render(request,'manager/index.html')


def courses(request):
    courses = Course.objects.all()
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            courses = Course.objects.all()
            return render(request, 'manager/courses.html', {'form': CourseForm(), 'success':'yes', 'courses': courses})
        else:
            return render(request, 'manager/courses.html', {'form': form, 'courses': courses})
    else:
       return render(request, 'manager/courses.html', {'form': CourseForm(), 'courses': courses})
    
 
def edit_course(request, cid):
    form = CourseForm(request.POST)
    course = Course.objects.get(id=cid)
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            course = Course.objects.filter(id=cid).update(name=data['name'], code=data['code'])

            return render(request, 'manager/courses.html', {'success':True})
        else:
            return render(request, 'manager/courses.html')
    else:
        data = {
                'name': course.name,
                'code': course.code
               }
        # course_id = Course.objects.get(id = cid)
        form = CourseForm()   
        return render(request,'manager/courses.html',{'form':CourseForm(initial=data)})


def delete_course(request):
    courses = Course.objects.all()
    if request.POST:
        course = Course.objects.filter(id__in = request.POST.getlist('items'))
        for cid in course:
            cid.delete()
        return render(request, 'manager/courses.html',{'courses':courses})

    # else:
    #     return render(request,'manager/courses.html',{'courses':courses})

def add_student(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
             data = form.cleaned_data
             user = User.objects.create(first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        username=data['username'])
             user.set_password(data['password'])
             user.student.student_code = data['student_code']
             user.student.national_code = data['national_code']
             user.student.address = data['address']
             user.student.cellphone_number = data['cellphone_number']
             user.student.major = data['major']
             user.student.save()
             user.save()
             #print user


             return render(request,'manager/add.html',{'form':StudentForm(),'success':'yes'})
        else:
            return render(request,'manager/add.html',{'form':form})
    else:
        return render(request,'manager/add.html',{'form':StudentForm()})


def edit_student(request, sid):
    # user = request.user
    student = Student.objects.get(id=sid)
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user=User.objects.filter(username=request.user.username).update(first_name=data['first_name'],
                                                                   last_name=data['last_name'],
                                                                   username=data['student_code'],
                                                                   password=data['password']
                                                                   )
            student.user.student_code = data['student_code']
            student.user.national_code = data['national_code']
            student.user.address = data['address']
            student.user.cellphone_number = data['cellphone_number']
            student.user.major = data['major']
            student.user.save()

            return render(request,'manager/students.html')
        else:
            return render(request,'manager/students.html',{'form':form})

    else:
        data = { 'first_name':student.user.first_name,
                 'last_name':student.user.last_name,
                 'username':student.user.username,
                 'password':student.user.password,
                 'student_code':student.student_code,
                 'national_code':student.national_code,
                 'address':student.address,
                 'cellphone_number':student.cellphone_number,
                 'major':student.major
                }
      
        form = StudentForm()
      
        return render(request,'manager/students.html',{'form':StudentForm(initial=data)})
        

def change_password(request, uid):
    if request.POST:
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['new_password'] == data['new_password_confirmation']:
                user = User.objects.get(id=uid)
                user.set_password(request.POST['new_password'])
                user.save()

                return render(request,'manager/change_password.html',{'form':ChangePasswordForm(), 'success_pass':'yes'})
            else:
                return render(request,'manager/change_password.html',{'form':ChangePasswordForm(), 'different_password':'yes'})
        else:
            return render(request,'manager/change_password.html' ,{'form':form})
    else:
        return render(request,'manager/change_password.html',{'form':ChangePasswordForm()})



def search_form(request):
    if request.POST:
        form = search_form(request.POST)
        if form:
            input = form.cleaned_data
            results = Student.objects.filter()

            return render(request,'manager/search_results.hrml')

    else:
        form = search_form(request.POST)
        return render(request,'manager/index.html',{'form':form})

def search(request):
    if request.POST:
        query = request.POST('q','')
        if query:
            qset = (
            Q(student_code__icontains=query) |
            Q(major__icontains=query)
            # Q(first_name__icontains = query)
                )
            results = Student.objects.filter(qset)
            return render(request,'manager/search_results.html',{'results':results,'query':query})
        else:
            results =[]
            return render(request,'manager/search_results.html',{'results':results,'query':query})
    else:
        print'gggg'
        return render(request,'manager/index.html')






def students(request):
   students = Student.objects.all()
   return render(request, 'manager/students.html',{'students':students})


def teachers(request):
   teacher = Teacher.objects.all()
   if request.POST:
      form = TeacherForm()
      if form.is_valid():
             data = form.cleaned_data
             user = User.objects.create(first_name = data['first_name'],
                                        last_name = data['last_name'],
                                        username = data['username'],
                                        email = data['data'])
             user.set_password(data['password'])
             user.teacher.teacher_code = data['teacher_code']
             user.teacher.national_code = data['national_code']
             user.teacher.address = data['address']
             user.teacher.cellphone = data['cellphone']
             user.teacher.major = data['major']
             user.teacher.grade = data['grade']
             user.save()
             return render(request,'manager/teachers.html',{'form':TeacherForm(),'success':'yes','teacher':teacher})
      else:
          return render(request,'manager/teachers.html',{'form':form, 'teacher':teacher})
   else:
       return render(request,'manager/teachers.html',{'form':TeacherForm(),'teacher':teacher})


def logout(request):
    logout(request)
    return render(request,'university/index.html')
