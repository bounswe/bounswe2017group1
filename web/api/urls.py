from django.conf.urls import url, include
from django.contrib import admin

from api.controller import (
    profile, comment, vote, user,
    heritage, tag, search,recommendation
)
urlpatterns = [

    # USER ROUTES
    url(r'^users/signup/?$', user.signup),
    url(r'^users/signin/?$', user.signin),
    url(r'^users/signout/?$', user.signout),
    url(r'^users/?$', user.users),
    url(r'^users/login_req/?$', user.login_required),


    # ITEM ROUTES
    url(r'^items/?$', heritage.heritage_get_post),
    url(r'^items/(?P<heritage_id>[0-9]+)/?$', heritage.heritage_get_put_delete),
    url(r'^items/(?P<heritage_id>[0-9]+)/comments/?$', heritage.get_all_comments),
    url(r'^items/(?P<heritage_id>[0-9]+)/tags/?$', heritage.get_all_tags),
    #url(r'^items/get_first/?$', heritage.heritage_get_first),


    # COMMENT ROUTES
    url(r'^comments/?$', comment.comment_get_post),
    url(r'^comments/(?P<comment_id>[0-9]+)/?$', comment.comment_get_put_delete),


    # VOTE ROUTES
    url(r'^votes/?$', vote.vote_post),


    # PROFILE ROUTES
    url(r'^profiles/?$', profile.profile_get_all),
    url(r'^profiles/(?P<user_id>[0-9]+)/?$', profile.profile_get),


    # TAG ROUTES
    url(r'^tags/?$', tag.list_all_tags),
    url(r'^tags/(?P<tag_id>[0-9]+)/heritages/?$', tag.get_all_heritage_items_own_this_tag),


    # SEARCH ROUTES
    url(r'^search/?$', search.search),
    #url(r'^search/advanced/?$', search.advanced_search),

    #RECOMMENDATION ROUTES
    url(r'^rec/tag/?$', recommendation.get_all_items_same_tag_with_heritage_that_user_created),
    url(r'^rec/upvote/?$', recommendation.get_all_items_that_user_upvoted),
    url(r'^rec/all/?$', recommendation.get_all_recommendations_tag_upvote_related),

]

