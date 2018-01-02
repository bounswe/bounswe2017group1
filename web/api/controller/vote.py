"""
    This controller handles the routing for votes of heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.model.profile import Profile
from api.model.vote import Vote
from api.model.heritage import Heritage
from api.serializer.vote import VoteSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST','DELETE'])
@permission_classes((IsAuthenticated,))
def vote_post_delete(request):
    """
    make an upvote or downvote
    or
    get back the vote

    :param request: client request
    :return: the created or deleted vote
    :return: only status_code
    :rtype: JSONObject
    """
    username = request.user.username
    request.data['voter'] = Profile.objects.filter(username=username).first().pk
    old_vote = Vote.objects.filter(voter=request.data['voter'],
                                   heritage=request.data['heritage']).first()
    if request.method == 'POST':

        serializer = VoteSerializer(instance=old_vote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            votes = Vote.objects.filter(heritage=request.data['heritage'])
            upvote_count = votes.filter(value=True).count()
            downvote_count = votes.filter(value=False).count()
            data = serializer.data
            data['upvote_count'] = upvote_count
            data['downvote_count'] = downvote_count
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if old_vote:
            old_vote.delete()
            votes = Vote.objects.filter(heritage=request.data['heritage'])
            upvote_count = votes.filter(value=True).count()
            downvote_count = votes.filter(value=False).count()
            data = {}
            data['upvote_count'] = upvote_count
            data['downvote_count'] = downvote_count
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_412_PRECONDITION_FAILED)


