"""
    This controller handles the routing for heritage items
"""
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response

from api.model.media import Media

from api.serializer.media import MediaSerializer

@api_view(['POST'])
@parser_classes((MultiPartParser, FormParser,))
def media_post(request):
    serializer = MediaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def media_get(request,pk):
    try:
        media = Media.objects.get(id=pk)
        serializer = MediaSerializer(media)
        return Response(serializer.data)
    except Media.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

