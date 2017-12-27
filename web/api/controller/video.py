"""
    This controller handles the routing for media items
"""
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes,authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from api.service import permission
from django.shortcuts import get_object_or_404

from api.model.video import Video

from api.serializer.video import VideoSerializer

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def video_post(request):
    video = None
    if(request.data["heritage"]):
        video = Video.objects.filter(heritage = request.data["heritage"]).first()
    serializer = VideoSerializer(instance=video, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def video_get_delete(request, pk):
    try:
        video = Video.objects.get(id=pk)
        heritage = video.heritage
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    elif request.method == 'DELETE' and permission.isOwner(request, obj=heritage):
         video.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_412_PRECONDITION_FAILED)

@api_view(['DELETE'])
@permission_classes((AllowAny, ))
def video_backdoor_delete(request, pk):
    try:
        video = Video.objects.get(id=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
         video.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_412_PRECONDITION_FAILED)

