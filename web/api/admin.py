# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.model.heritage import Heritage
from api.model.profile import Profile
from api.model.comment import Comment
from api.model.vote import Vote
from api.model.tag import Tag
from api.model.media import Media

# Register your models here.
admin.site.register(Heritage)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Tag)
admin.site.register(Media)
