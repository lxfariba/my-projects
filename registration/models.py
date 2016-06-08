from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.conf import settings
from time import time
#from django.contrib.auth.models import User

WEEK_CHOICES = (
            ('Mon','Monday'),
            ('Tue','Tuesday'),
            ('Wed','Wednesday'),
            ('Thu','Thursday'),
            ('Fri','Friday'),
            ('Sat','Saturday')  
)


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True)
    student_code = models.IntegerField( blank=True, null=True)
    national_code = models.IntegerField(blank=True, null=True)
    address = models.TextField()
    cellphone_number = models.PositiveIntegerField(blank=True, null=True)
    major = models.CharField(max_length=300)
    image_profile = models.ImageField(upload_to='avatars')

    def __unicode__(self):
        return self.major


def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.get_or_create(user=instance)

post_save.connect(create_student, sender=settings.AUTH_USER_MODEL)

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True) 
    teacher_code = models.IntegerField(null=True)
    national_code = models.IntegerField(null=True)
    address = models.TextField()
    cellphone = models.PositiveIntegerField(null=True)
    major = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)


def create_teacher(sender, instance, created, **kwargs):
    if created:
        Teacher.objects.get_or_create(user=instance)
post_save.connect(create_teacher, sender=settings.AUTH_USER_MODEL)         
