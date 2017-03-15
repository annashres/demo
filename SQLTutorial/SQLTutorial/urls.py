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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^professors', app.views.professors_list, name='professors_list'), 
    url(r'^departments', app.views.departments_list, name='departments_list'), 
    url(r'^courses', app.views.courses_list, name='courses_list'), 
    url(r'^course/(?P<pk>\d+)/$', app.views.courses_detail, name='courses_detail'), 
    url(r'^students', app.views.students_list, name='students_list'), 
    url(r'^reviews', app.views.reviews_list, name='reviews_list'), 
    url(r'^review/new', app.views.new_review, name='new_review'), 
    url(r'^done', app.views.done, name='done'), 
]
