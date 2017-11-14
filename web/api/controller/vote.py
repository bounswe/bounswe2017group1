from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.model.profile import Profile
from api.model.vote import Vote
from api.serializer.vote import VoteSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def vote_post(request):
    username = request.user.username
    request.data['voter'] = Profile.objects.filter(username=username).first().pk
    old_vote = Vote.objects.filter(voter=request.data['voter'],
                                   heritage=request.data['heritage']).first()
    serializer = VoteSerializer(instance=old_vote, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
