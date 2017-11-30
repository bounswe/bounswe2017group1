"""
    This controller handles the routing for heritage items
"""
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes,authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from api.service import permission

from api.model.media import Media

from api.serializer.media import MediaSerializer

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
@parser_classes((MultiPartParser, FormParser,))
def media_post(request):
    serializer = MediaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes((IsAuthenticated,))
def media_get_delete(request, pk):
    try:
        media = Media.objects.get(id=pk)
        heritage = media.heritage
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MediaSerializer(media)
        return Response(serializer.data)

    elif request.method == 'DELETE' and permission.isOwner(request, obj=heritage):
         media.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_412_PRECONDITION_FAILED)
