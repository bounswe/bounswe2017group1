from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from UniversityApp import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'UniversityAPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/', views.StudentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)