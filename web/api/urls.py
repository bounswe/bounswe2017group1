
from django.conf.urls import url, include
from django.contrib import admin

from api.controller import user

urlpatterns = [
    # USER ROUTES
    url(r'^users/signup$', user.signup),
    url(r'^users/signin$', user.signin),
    url(r'^users/signout$', user.signout),
    url(r'^users$', user.users),
    #url(r'^users/(?P<userId>[0-9]+)$', user.user),
    #url(r'^users/me$', user.me),
    #url(r'^users/me/history$', user.history),
    #url(r'^users/me/restaurantHistory$', user.restaurantHistory),
]