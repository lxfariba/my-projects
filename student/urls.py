from django.conf.urls import url

from student.views import views



urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^login_students/$',views.login_student,name='login'),
    url(r'^profile_student/$',views.profile,name='profile'),
    url(r'^image_profile/$',views.image_profile,name = 'image_profile'),
    # url(r'^image_profile/$',views.display_image,name = 'display_profile'),
    url(r'^change_password/$',views.change_password,name='change_password'),

]
