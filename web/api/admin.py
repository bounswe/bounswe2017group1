# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from api.model.heritage import Heritage
from api.model.profile import Profile
from api.model.comment import Comment
from api.model.vote import Vote
from api.model.tag import Tag
from api.model.media import Media


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'location', 'gender', 'photo_path')


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    inlines = [ProfileInline]


class HeritageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator_id', 'location')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'heritage', 'creator')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'related_list')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'voter', 'heritage')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Heritage, HeritageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Media)
