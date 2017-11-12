"""
    This controller handles the routing for heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from api.model.heritage import Heritage
from api.model.profile import Profile
from api.model.comment import Comment
from api.model.tag import Tag
from api.serializer.heritage import HeritageSerializer
from api.serializer.comment import CommentSerializer
from api.serializer.tag import TagSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def heritage_get_post(request):

    if request.method == 'GET':
        try:
            serializer = HeritageSerializer(Heritage.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':

        username = request.user.username
        request.data['creator'] = Profile.objects.filter(username=username).first().pk

        serializer = HeritageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def heritage_get_put_delete(request, heritage_id):
    try:
        heritage = Heritage.objects.get(id=heritage_id)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HeritageSerializer(heritage)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        username = request.user.username
        request.data['creator'] = Profile.objects.filter(username=username).first().pk

        serializer = HeritageSerializer(instance=heritage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            heritage.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_all_comments(request, heritage_id):
    try:
        comments = Comment.objects.all().filter(heritage=heritage_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_tags(request, heritage_id):
    try:
        tags = Heritage.objects.get(id=heritage_id).tags
        serializer = TagSerializer(tags)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def heritage_get_first(request):
    try:
        heritage = Heritage.objects.first()
        # print(heritage.creator)
        serializer = HeritageSerializer(heritage)
        return Response(serializer.data)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)