# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import get_template
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect, render_to_response, render
from django.contrib.auth import authenticate, login, logout
#from django.views import generic
#from django.views.generic import View
#from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required

def Home(request):
    now = datetime.datetime.now()
    t = get_template('homepage.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)

def Register(request):
    username = request.GET['username']
    password = request.GET['password']

    user = User.objects.create_user(username=username, password=password)
    user.save()

    #print User.objects.all()
    #userProfile = UserProfile.objects.create(user=user, location="Konya")
    #userProfile.save()
    #print UserProfile.objects.all()

    return HttpResponse("register user {}".format(user.username))


#TODO: implement login machanism here
def Login(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        print "login succesfully"
        return HttpResponse("login as {}".format(user.username))
    else:
        # Return an 'invalid login' error message.
        print "no such user"
        return redirect('/home/')

def Logout(request):
    username = request.user.username
    logout(request)
    return HttpResponse("logout as {}".format(username))

@login_required(login_url='/home/')
def Profile(request):
    return HttpResponse("Profile {}".format(request.user.username))