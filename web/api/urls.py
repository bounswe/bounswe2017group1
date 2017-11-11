from django.conf.urls import url, include
from django.contrib import admin

from api.controller import (
    profile, comment, vote, user,
    heritage, tag, search
)

urlpatterns = [

    # USER ROUTES
    url(r'^users/signup/?$', user.signup),
    url(r'^users/signin/?$', user.signin),
    url(r'^users/signout/?$', user.signout),
    url(r'^users/?$', user.users),
    url(r'^users/login_req/?$', user.login_required),

    # ITEM ROUTES
    url(r'^items/?$', heritage.heritage_post),
    url(r'^items/get_first/?$', heritage.heritage_get_first),
    url(r'^items/(?P<pk>[0-9]+)/?$', heritage.heritage_get_put_delete),
    url(r'^items/all/?$', heritage.heritage_get_all),

    # COMMENT ROUTES
    url(r'^comments/?$', comment.comment_post),
    url(r'^comments/(?P<pk>[0-9]+)/?$', comment.comment_get_put_delete),
    url(r'^comments/all?$', comment.comment_get_all),
    url(r'^heritagecomments/(?P<pk>[0-9]+)/?$', comment.comment_get_heritage),

    # VOTE ROUTES
    url(r'^votes/?$', vote.vote_post),

    # PROFILE ROUTES
    url(r'^profiles/(?P<pk>[0-9]+)/?$', profile.profile_get),
    url(r'^profiles/all/?$', profile.profile_get_all),

    # TAG ROUTES
    url(r'^tags/all?$', tag.list_all_tags),
    url(r'^tags/all_tags/(?P<pk_heritage>[0-9]+)/?$', tag.get_all_tags_of_heritage_item),
    url(r'^tags/all_heritages/(?P<pk_tag>[0-9]+)/?$', tag.get_all_heritage_items_own_this_tag),

    # SEARCH ROUTES
    url(r'^search/location/(?P<location>[a-zA-Z]+)/?$', search.searchItemByLocation),
    url(r'^search/creator/(?P<creator>\w+)/?$', search.searchItemByCreator),
    url(r'^search/title/(?P<title>\w+)/?$', search.searchItemByTitle),

]
