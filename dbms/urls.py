"""dbms URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from course_management import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/', include('course_management.urls')),
	url(r'^instructor_reg/',views.instructor_reg,name='instructor_reg'),
	url(r'^student_reg/',views.student_reg,name='student_reg'),
	url(r'^logged_out/',views.log_out,name='log_out'),
	url(r'^home/',views.home,name='home'),
	url(r'^registration/',views.registration,name='registration'),
	url(r'^course_reg/',views.course_reg,name='course_reg'),
	url(r'^attendance/',views.attendance,name='attendance'),
	url(r'^grade/',views.grade,name='grade'),
	url(r'^feedback/',views.feedback,name='feedback'),
	url(r'^student_display/',views.stud_display,name='stud_display'),
	url(r'^view_feedback/',views.view_fb,name='view_feedback'),
	# above maps any URLs starting
	# with rango/ to be handled by
	# the rango application
    	url(r'^admin/', admin.site.urls),
]
