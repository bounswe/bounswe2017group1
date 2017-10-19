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
from django.utils.decorators import method_decorator


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import UserSeralizer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSeralizer

@method_decorator(login_required, name='UserDetail')
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSeralizer


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


"""
class UserList2(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSeralizer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail2(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(username=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSeralizer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSeralizer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""

"""
class UserList3(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSeralizer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserDetail3(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSeralizer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

"""

"""
@csrf_exempt
@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSeralizer(users, many=True)
        return Response(serializer.data)
        #return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return JsonResponse(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):

    try:
        user = User.objects.get(username=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        #return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSeralizer(user)
        return Response(serializer.data)
        #return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSeralizer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""