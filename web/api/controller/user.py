import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



from ..serializer.user import  UserSerializer
from ..serializer.profile import  ProfileSerializer

from ..service import user as UserService

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def signup(request):
    """
    Create user and return
    """
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_id = user_serializer.save().id
        user = authenticate(
            request,
            username=user_serializer.validated_data['username'],
            password=user_serializer.validated_data['password']
        )
        token = UserService.refreshToken(user)

        request.data['user'] = user_id
        profile_serializer = ProfileSerializer(data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            data = {
                "user": user_serializer.data,
                "profile": profile_serializer.data,
                "token": token.key
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def signin(request):
    """
    authenticate user with email and password, return token
    """

    #print request.data

    serializer = UserSerializer(data=request.data)

    #serializer.is_valid()

    if serializer.is_valid():

        #print serializer.validated_data['password']

        user = authenticate(
            request,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user is not None:
            token = UserService.refreshToken(user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def signout(request):
    """
    delete user token from database
    """
    if request.user:
        UserService.deleteToken(request.user)
        return Response(status=status.HTTP_200_OK)
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def users(request):
    """
    retrieve all users
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def login_required(req):
    if(req.user.is_authenticated()):
        data = {
            "username": req.user.username
        }
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
