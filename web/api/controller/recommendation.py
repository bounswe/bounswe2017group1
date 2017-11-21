from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from django.db.models import Q

from api.model.vote import Vote
from api.model.heritage import Heritage
from api.model.profile import Profile
from api.serializer.heritage import HeritageSerializer

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_all_items_same_tag_with_heritage_that_user_created(request):
    names_of_heritage_tags = []
    if request.method == 'GET':
        try:
            context = {}
            if request.user.username:
                print request.user.username
                profile_id = Profile.objects.filter(username=request.user.username).first().pk
                heritage_tags = Heritage.objects.filter(creator=profile_id)
                context['requester_profile_id'] = profile_id
                for h in heritage_tags:
                    for t in h.tags.all():
                        names_of_heritage_tags.append(t.name)
                #Making distinct list of tags
                names_of_heritage_tags = list(set(names_of_heritage_tags))

                """This function do:
                    * Get all heritage items that this user created.
                    * Get all tags of heritage items that this user owns.
                    * Get all heritage items that these tags included in.
                    * Exclude the heritage items which this current user created.
                    * Returns heritage items, distinctly!
                """
                serializer = HeritageSerializer(Heritage.objects.all().filter(tags__name__in=names_of_heritage_tags).exclude(creator=profile_id).distinct(), context=context, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_all_items_that_user_upvoted(request):
    heritage_ids = []
    if request.method == 'GET':
        try:
            context = {}
            if request.user.username:
                print request.user.username
                profile_id = Profile.objects.filter(username=request.user.username).first().pk

                #Take only UP votes
                votes = Vote.objects.filter(voter=profile_id, value=True)
                context['requester_profile_id'] = profile_id

                for v in votes:
                    heritage_ids.append(v.heritage.id)

                """This function do:
                    * Get all heritage items that this user upvoted.
                    * Exclude the heritage items which this current user created.
                    * Returns heritage items, distinctly!
                """
                serializer = HeritageSerializer(Heritage.objects.all().filter(id__in=heritage_ids).exclude(creator=profile_id).distinct(), context=context, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_all_recommendations_tag_upvote_related(request):
    names_of_heritage_tags = []
    heritage_ids = []
    if request.method == 'GET':
        try:
            context = {}
            if request.user.username:
                print request.user.username
                profile_id = Profile.objects.filter(username=request.user.username).first().pk
                heritage_tags = Heritage.objects.filter(creator=profile_id)
                votes = Vote.objects.filter(voter=profile_id, value=True)

                context['requester_profile_id'] = profile_id

                for h in heritage_tags:
                    for t in h.tags.all():
                        names_of_heritage_tags.append(t.name)
                for v in votes:
                    heritage_ids.append(v.heritage.id)
                names_of_heritage_tags = list(set(names_of_heritage_tags))

                serializer = HeritageSerializer(Heritage.objects.all().
                                                filter(Q(tags__name__in=names_of_heritage_tags) | Q(id__in=heritage_ids)).
                                                exclude(creator=profile_id).distinct(), context=context, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)





