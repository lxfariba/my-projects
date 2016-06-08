
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from university.views import views


urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^manager/',include('manager.urls',namespace='manager')),
    url(r'^student/',include('student.urls',namespace='student')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.MEDIA_ROOT})]
