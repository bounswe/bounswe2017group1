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

@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes((MultiPartParser, FormParser))
def signup(request):
    """
    Create user and return
    """
    mutable = request.POST._mutable
    request.POST._mutable = True  # make the request mutable so that I can add extra fields
    user_serializer = UserSerializer(data=request.data)

    if user_serializer.is_valid():
        user = user_serializer.save()
        request.data['user'] = user.id
        request.data['username'] = user.username
        request.POST._mutable = mutable  # leave as you wish to find :)

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


@api_view(['POST'])
@permission_classes((AllowAny,))
def signin(request):
    """
    authenticate user with email and password, return token
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
    delete user token from database
    """
    UserService.deleteToken(request.user)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def users(request):
    """
    retrieve all users
    """
    try:
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def login_required(req):
    data = {
        "username": req.user.username
    }
    return Response(data, status=status.HTTP_200_OK)
