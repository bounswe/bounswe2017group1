from django.conf.urls import url, include
from django.contrib import admin

from api.controller import (
    profile, comment, vote, user,
    heritage, tag, search, media,
    recommendation, annotation
)

urlpatterns = [

    # USER ROUTES
    url(r'^users/signup/?$', user.signup),
    url(r'^users/signin/?$', user.signin),
    url(r'^users/signout/?$', user.signout),
    url(r'^users/?$', user.users),
    url(r'^users/login_req/?$', user.login_required),
    url(r'^users/image/?$', user.add_or_change_image),

    # ITEM ROUTES
    url(r'^items/?$', heritage.heritage_get_post),
    url(r'^items/(?P<heritage_id>[0-9]+)/?$', heritage.heritage_get_put_delete),
    url(r'^items/(?P<heritage_id>[0-9]+)/comments/?$', heritage.get_all_comments),
    url(r'^items/(?P<heritage_id>[0-9]+)/tags/?$', heritage.get_all_tags),
    url(r'^items/new/?$', heritage.get_new_heritages),
    url(r'^items/top/?$', heritage.get_top_heritages),
    url(r'^items/trending/?$', heritage.get_trending_heritages),
    #url(r'^items/get_first/?$', heritage.heritage_get_first),


    # COMMENT ROUTES
    url(r'^comments/?$', comment.comment_get_post),
    url(r'^comments/(?P<comment_id>[0-9]+)/?$', comment.comment_get_put_delete),
    url(r'^comments/backdoor/(?P<comment_id>[0-9]+)/?$', comment.comment_bacdoor_delete),

    # VOTE ROUTES
    url(r'^votes/?$', vote.vote_post_delete),


    # PROFILE ROUTES
    url(r'^profiles/?$', profile.profile_get_all),
    url(r'^profiles/(?P<user_id>[0-9]+)/?$', profile.profile_get),


    # TAG ROUTES
    url(r'^tags/?$', tag.list_all_tags),
    url(r'^tags/(?P<tag_id>[0-9]+)/heritages/?$', tag.get_all_heritage_items_own_this_tag),

    #MEDIA ROUTES
    url(r'^medias/(?P<pk>[0-9]+)/?$', media.media_get_delete),
    url(r'^medias/backdoor/(?P<pk>[0-9]+)/?$', media.media_backdoor_delete),

    url(r'^medias/?$', media.media_post),


    # SEARCH ROUTES
    url(r'^search/?$', search.search),
    #url(r'^search/advanced/?$', search.advanced_search),

    #RECOMMENDATION ROUTES
    url(r'^recommendation/user/?$', recommendation.user_based_alternative),
    url(r'^recommendation/heritage/(?P<item_id>[0-9]+)/?$', recommendation.heritage_based_alternative),
    #url(r'^recommendation/test/(?P<item_id>[0-9]+)/?$', recommendation.recommendation_test),


    #ANNOTATION ROUTES
    url(r'^annotation/?$', annotation.get_all),
    url(r'^annotation/heritage/(?P<item_id>[0-9]+)/?$', annotation.create_on_description_or_get),
    url(r'^annotation/heritage/(?P<item_id>[0-9]+)/media/(?P<media_id>[0-9]+)/?$', annotation.create_annotation_on_media),
    url(r'^annotation/heritage/(?P<item_id>[0-9]+)/comment/(?P<comment_id>[0-9]+)/?$', annotation.create_annotation_on_comment),

]
