from django.conf.urls import url
from CulturalHeritage import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    #url(r'^home/$', views.Home ,name='home'),
    url(r'^users/signup/$', views.SignUp ,name='signup'),
    url(r'^users/signin/$', views.SignIn, name='signin'),
    #url(r'^logout/$', views.Logout, name='logout'),
    #url(r'^profile/$', views.Profile, name='profile'),

    #url(r'^users/$', views.user_list),
    #url(r'^users/(?P<pk>[a-zA-Z0-9]+)/$', views.user_detail),

    url(r'^users/$', views.UserList2.as_view()),
    url(r'^users/(?P<pk>[a-zA-Z0-9]+)/$', views.UserDetail2.as_view()),
    #url(r'^obtain-auth-token/$', csrf_exempt(obtain_auth_token))

]

urlpatterns = format_suffix_patterns(urlpatterns)