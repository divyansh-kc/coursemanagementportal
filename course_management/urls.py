from django.conf.urls import url
from course_management import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
