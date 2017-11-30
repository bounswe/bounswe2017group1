"""
    This controller handles the routing for heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.model.profile import Profile

from api.model.comment import Comment
from api.serializer.comment import CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from api.service import permission


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def comment_get_post(request):

    if request.method == 'GET':
        try:
            context = {}
            if request.user.username:
                profile_id = Profile.objects.filter(username=request.user.username).first().pk
                context['requester_profile_id'] = profile_id
            serializer = CommentSerializer(Comment.objects.all(),context=context, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST' and request.user.is_authenticated:
        username = request.user.username
        context = {}
        profile_id = Profile.objects.filter(username=username).first().pk
        context['requester_profile_id'] = profile_id
        request.data['creator'] = profile_id
        serializer = CommentSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def comment_get_put_delete(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        context = {}
        if request.user.username:
            profile_id = Profile.objects.filter(username=request.user.username).first().pk
            context['requester_profile_id'] = profile_id
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment, context = context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE' and permission.isOwner(request, obj=comment):
        try:
            comment.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_412_PRECONDITION_FAILED)