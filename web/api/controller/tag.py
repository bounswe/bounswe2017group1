"""
    This controller handles the routing for tag of heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.model.profile import Profile
from api.model.tag import Tag
from api.model.heritage import Heritage
from api.serializer.tag import TagSerializer
from api.serializer.heritage import HeritageSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny


@api_view(['GET'])
@permission_classes((AllowAny, ))
def list_all_tags(request):
    """
    get all tags

    :param request: client request
    :return: list of all tags
    :rtype: JSONArray
    """
    try:
        serializer = TagSerializer(Tag.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_all_heritage_items_own_this_tag(request, tag_id):
    """
    get all heritage items which has the indicated tag

    :param request: client request
    :param tag_id: indicates the tag
    :return: list of all heritage items which has the indicated tag
    :rtype: JSONArray
    """
    try:
        heritage = Heritage.objects.get(tags__id=tag_id)
        serializer = HeritageSerializer(heritage)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
