"""
    This controller handles the routing for heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.model.heritage import Profile
from api.serializer.profile import ProfileSerializer


@api_view(['GET'])
def profile_get(request, pk):
    print(pk)
    try:
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def profile_get_all(request):
    try:
        serializer = ProfileSerializer(Profile.objects.all(), many=True)
        return Response(serializer.data)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
