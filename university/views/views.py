from django.shortcuts import render
from registration.models import Course


def home(request):
   courses = Course.objects.all()
   return render(request, 'university/index.html',{'courses':courses})
 
