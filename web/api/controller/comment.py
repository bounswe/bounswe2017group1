"""
    This controller handles the routing for heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.model.profile import Profile

from api.model.comment import Comment
from api.serializer.comment import CommentSerializer


@api_view(['POST'])
def comment_post(request):
    username = request.user.username
    request.data['creator'] = Profile.objects.filter(username=username).first().pk
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_get_put_delete(request, pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        username = request.user.username
        request.data['creator'] = Profile.objects.filter(username=username).first().pk

        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_get_all(request):
    try:
        serializer = CommentSerializer(Comment.objects.all(), many=True)
        return Response(serializer.data)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def comment_get_heritage(request, pk):
    try:
        serializer = CommentSerializer(Comment.objects.all().filter(heritage=pk), many=True)
        return Response(serializer.data)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
