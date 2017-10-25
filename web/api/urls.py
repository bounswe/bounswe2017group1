
from django.conf.urls import url, include
from django.contrib import admin

from api.controller import user
from api.controller import item
from api.controller import profile


urlpatterns = [
    # USER ROUTES
    url(r'^users/signup/?$', user.signup),
    url(r'^users/signin/?$', user.signin),
    url(r'^users/signout/?$', user.signout),
    url(r'^users/?$', user.users),
    url(r'^users/login_req/?$', user.login_required),

    url(r'^items/?$', item.heritage_post),
    url(r'^items/get_first/?$', item.heritage_get_first), #for test purposes returns one heritage item

    url(r'^items/(?P<pk>[0-9]+)/?$', item.heritage_get),
    url(r'^items/all$', item.heritage_get_all),

    url(r'^profiles/(?P<pk>[0-9]+)/?$', profile.profile_get),
    url(r'^profiles/all/?$', profile.profile_get_all),


]
