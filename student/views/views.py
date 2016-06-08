from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
import uuid
from PIL import Image as PILImage
from registration.models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from student.forms import LoginStudentForm,ProfileStudent, ChangePasswordForm, ImageProfileForm


def home(request):
    return render(request, 'student/index.html')


def login_student(request):
    if request.POST:
        form = LoginStudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            #print user
            if user:
                login(request, user)
                return render(request, 'student/profile_student.html')
            else:
                return render(request, 'student/login_students.html', {'form':LoginStudentForm(), 'false': True})
        else:
            return render(request, 'student/login_students.html', {'form':form})
    else:

        return render(request, 'student/login_students.html', {'form':LoginStudentForm()})


def profile(request):
    user = request.user
    if request.POST:
        form = ProfileStudent(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.filter(username=request.user.username).update(first_name=data['first_name'],
                                                                       last_name=data['last_name']
                                                                      )
            user.student.student_code = data['student_code']
            user.student.national_code = data['national_code']
            user.student.major = data['major']
            user.student.cellphone_number = data['cellphone_number']
            user.student.address = data['address']
            user.student.save()

            return render(request,'student/profile_student.html',{'success':True})
        else:
            return render(request,'student/profile_student.html',{'form':form})
    else:
        data = {
            'first_name':user.first_name,
            'last_name':user.last_name,
            'student_code':user.student.student_code,
            'national_code':user.student.national_code,
            'major':user.student.major,
            'cellphone_number':user.student.cellphone_number,
            'address':user.student.address
        }
        return render(request,'student/profile_student.html',{'form':ProfileStudent(initial=data)})


def profile_student(request):
    return render(request,'student/profile_student.html')


def image_profile(request,width=250,height=250):
    if request.POST:
        form = ImageProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if request.FILES.get('image_profile'):

                avatar_path = settings.AVATAR_ROOT+str(request.user.id)+'.jpg'

                avatar = open(avatar_path, 'wb')
                for chunk in request.FILES['image_profile'].chunks():
                    avatar.write(chunk)
                avatar.close()
                if width or height:
                    pil_img = PILImage.open(avatar_path)
                    if pil_img.mode !='RGB':
                        pil_img = pil_img.convert('RGB')
                    pil_img.resize((width,height),PILImage.ANTIALIAS).save(avatar_path,format='JPEG')

                request.user.student.image_profile = settings.AVATAR_PATH +str(request.user.id)+'.jpg'
                request.user.student.save()
                return render(request, 'student/image_profile.html')
            else:
                return render(request,'student/image_profile.html',{'form':form},{'message':True})
    else:
        img = Student.objects.get(user= request.user)
        return render(request,'student/image_profile.html',{'form':ImageProfileForm(request),'img':img})



def change_password(request):
     if request.POST:
        form = ChangePasswordForm(request, request.POST)
        #print form
        if form.is_valid():
            request.user.set_password(request.POST['password_con'])
            request.user.save()
            user = authenticate(username=request.user.username, password=request.POST['password_con'])
            # print user
            login(request, user)
            return render(request,'student/change_password.html',{'success':'yes'})
        else:
            return render(request,'student/change_password.html',{'form':form})
     else:
         return render(request,'student/change_password.html',{'form':ChangePasswordForm(request)})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

