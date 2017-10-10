# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render


from django.template.loader import get_template
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect


def home_page(request):
    now = datetime.datetime.now()
    t = get_template('homepage.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)

#TODO: implement login machanism here
def authanticate(request):
    #if user is authanticated
    return redirect('/homepage')

def login_page(request):
    now = datetime.datetime.now()
    t = get_template('login.html')
    html = t.render({'current_date': now})
    return HttpResponse(html)