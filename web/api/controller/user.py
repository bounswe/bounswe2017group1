"""
    This controller handles the routing for login and registration system
"""

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from api.serializer.user import UserSerializer
from api.serializer.profile import ProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from api.service import user as UserService
from api.model.profile import Profile

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    """
    register the user

    :param request: client request
    :return: the user's data and profile
    :rtype: JSONObject
    """
    mutable = request.POST._mutable
    request.POST._mutable = True  # make the request mutable so that I can add extra fields
    user_serializer = UserSerializer(data=request.data)

    if user_serializer.is_valid():
        user = user_serializer.save()
        request.data['user'] = user.id
        request.data['username'] = user.username

        profile_serializer = ProfileSerializer(data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            data = {
                "user": user_serializer.data,
                "profile": profile_serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        request.POST._mutable = mutable  # leave as you wish to find :)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@parser_classes((MultiPartParser, FormParser))
@permission_classes((IsAuthenticated,))
def add_or_change_image(request):
    """
    edit the profile image of the user

    :param request: client request
    :return: profile of the user
    :rtype: JSONObject
    """
    profile = Profile.objects.filter(username=request.user.username).first()
    serializer = ProfileSerializer(instance=profile)
    if 'image' in request.data:
        Profile.objects.filter(username=request.user.username).update(image=request.data['image'])
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))
def signin(request):
    """
    authenticate user with email and password

    :param request: client request
    :return: Authorization Token
    :rtype: JSONObject
    """
    if 'username' in request.data and 'password' in request.data:

        user = authenticate(
            request,
            username=request.data['username'],
            password=request.data['password']
        )

        if user is not None:
            token = UserService.refreshToken(user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'user or password is wrong'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'username and password fields are required'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def signout(request):
    """
    delete the user token from database

    :param request: client request
    :return: only status_code
    """
    UserService.deleteToken(request.user)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def users(request):
    """
    retrieve all users

    :param request: client request
    :return: list of all users
    :rtype: JSONArray
    """
    try:
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def login_required(req):
    """
    test permission class and token

    :param req: client request
    :return: the requester username
    """
    data = {
        "username": req.user.username
    }
    return Response(data, status=status.HTTP_200_OK)
