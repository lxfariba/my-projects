from django.conf.urls import url

from manager.views import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^courses/$', views.courses,name='courses'), 
    url(r'^courses/edit/(\d+)/$', views.edit_course,name='edit_course'),
    url(r'^courses/delete/$',views.delete_course,name='delete_course'),
    url(r'^students/$', views.students,name='students'),
    url(r'^students/edit/(\d+)/$', views.edit_student,name='edit_student'), 
    url(r'^students/change/(\d+)/$',views.change_password,name='change_password'),
    url(r'^teachers/$', views.teachers,name='teachers'),
    url(r'^students/add/$', views.add_student,name='add'),
    # url(r'^search_form/$',views.search_form,name = 'search-form'),
    url(r'^search_results/?$',views.search, name = 'search'),


    # url(r'^login_students/$',views.login_student, name='login_students'),
    # url(r'^profile_student/$',views.profile_student, name='profile_student'),
    url(r'^$', views.logout, name='logout'),

]

