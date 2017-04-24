from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^students$', views.StudentList.as_view())
]
