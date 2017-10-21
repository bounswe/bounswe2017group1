
from django.conf.urls import url, include
from django.contrib import admin

from api.controller import user
from api.controller import item

urlpatterns = [
    # USER ROUTES
    url(r'^users/signup$', user.signup),
    url(r'^users/signin$', user.signin),
    url(r'^users/signout$', user.signout),
    url(r'^users$', user.users),
    url(r'^items/$', item.heritage_post),
    url(r'^items/(?P<pk>[0-9]+)/$', item.heritage_get),
    #url(r'^users/(?P<userId>[0-9]+)$', user.user),
    #url(r'^users/me$', user.me),
    #url(r'^users/me/history$', user.history),
    #url(r'^users/me/restaurantHistory$', user.restaurantHistory),
]
