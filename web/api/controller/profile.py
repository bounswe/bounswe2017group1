"""
    This controller handles the routing for heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.model.heritage import Profile
from api.serializer.profile import ProfileSerializer
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes((AllowAny, ))
def profile_get(request, user_id):
    try:
        profile = Profile.objects.get(id=user_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def profile_get_all(request):
    try:
        serializer = ProfileSerializer(Profile.objects.all(), many=True)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
