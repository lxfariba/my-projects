from django import forms

from registration.models import Course, Student


class CourseForm(forms.ModelForm):
     class Meta:
          model = Course
          exclude = [] 


class StudentForm(forms.Form):
     first_name = forms.CharField(max_length=100)
     last_name = forms.CharField(max_length=100)
     username = forms.CharField(max_length=100)
     password = forms.CharField(max_length=100)
     student_code = forms.IntegerField(required=False)
     national_code = forms.IntegerField(required=False)
     address = forms.CharField(max_length=100,widget=forms.Textarea)
     cellphone_number = forms.IntegerField(required=False)
     major = forms.CharField(max_length=100)


class ImageProfileForm(forms.Form):
     image_profile =forms.ImageField()


class SearchForm(forms.Form):
     search = forms.CharField(max_length = 100)

class TeacherForm(forms.Form):
     first_name = forms.CharField(max_length=100)
     last_name = forms.CharField(max_length=100)
     username = forms.CharField(max_length=100)
     password = forms.CharField(max_length=100)
     email = forms.EmailField()
     teacher_code = forms.IntegerField()
     national_code = forms.IntegerField()
     address = forms.CharField(max_length=100,widget=forms.Textarea)
     cellphone_number = forms.IntegerField()
     major = forms.CharField(max_length=100)
     grade = forms.CharField(max_length=100)


class ChangePasswordForm(forms.Form):
     new_password = forms.CharField(max_length=100)
     new_password_confirmation = forms.CharField(max_length=100)


