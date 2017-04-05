"""SQLTutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import app.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^professors/$', app.views.professors_list, name='professors_list'), 
    url(r'^professor/new/$', app.views.new_professor, name='new_professor'), 
    url(r'^professor/(?P<pk>\d+)/edit/$', app.views.edit_professor, name='edit_professor'),

    url(r'^students/$', app.views.students_list, name='students_list'),
    url(r'^student/new/$', app.views.new_student, name='new_student'), 

    url(r'^courses/$', app.views.courses_list, name='courses_list'), 
    url(r'^course/new/$', app.views.new_course, name='new_course'), 
    url(r'^course/(?P<pk>\d+)/$', app.views.course_detail, name='course_detail'),
    url(r'^course/(?P<pk>\d+)/edit/$', app.views.edit_course, name='edit_course'),
    url(r'^course/(?P<pk>\d+)/delete/$', app.views.delete_course, name='delete_course'),

]
