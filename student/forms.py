from django import forms
from django.contrib.auth import authenticate



class LoginStudentForm(forms.Form):
     username = forms.CharField(max_length=30)
     password= forms.CharField(max_length=30)


class ProfileStudent(forms.Form):
     first_name = forms.CharField(max_length=40)
     last_name = forms.CharField(max_length=40)
     student_code = forms.IntegerField()
     national_code = forms.IntegerField()
     major = forms.CharField(max_length=22)
     cellphone_number = forms.IntegerField(required=False)
     address = forms.CharField(max_length=50)


class ImageProfileForm(forms.Form):
     image_profile = forms.ImageField()


class ChangePasswordForm(forms.Form):
     old_password = forms.CharField(max_length=50)
     new_password = forms.CharField(max_length=50)
     password_con = forms.CharField(max_length=50)

     def __init__(self, request, *args, **kwargs):
          super(ChangePasswordForm, self).__init__(*args, **kwargs)
          self.request = request

     def clean_old_password(self):
          user = authenticate(user=self.request.user.username, password=self.cleaned_data['password'])
          #print user
          if not user:
               raise forms.ValidationError('your old password is not correct!')

          return self.cleaned_data['old_password']

     def clean_password_con(self):
          if self.cleaned_data['new_password'] != self.cleaned_data['password_con'] :
               raise forms.ValidationError("Your new passwords don't match!")

          return self.cleaned_data['password_con']
