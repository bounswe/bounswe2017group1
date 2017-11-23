from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from django.db.models import Q

from api.model.vote import Vote
from api.model.heritage import Heritage
from api.model.profile import Profile
from api.serializer.heritage import HeritageSerializer
from itertools import chain

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
                serializer = HeritageSerializer(Heritage.objects.all().
                                                filter(tags__name__in=names_of_heritage_tags).
                                                exclude(creator=profile_id).distinct(), context=context, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_all_items_that_user_upvoted_has_same_tags(request):
    heritage_tags = []
    tags_upvoted_items = []
    if request.method == 'GET':
        try:
            context = {}
            if request.user.username:
                print request.user.username
                profile_id = Profile.objects.filter(username=request.user.username).first().pk

                #Take only UP votes
                votes_include_heritages = Vote.objects.filter(voter=profile_id, value=True)
                context['requester_profile_id'] = profile_id

                for v in votes_include_heritages:
                    heritage_tags.append(v.heritage)

                for h in heritage_tags:
                    for t in h.tags.all():
                        tags_upvoted_items.append(t.name)

                """This function do:
                    * Get all heritage items that this user upvoted.
                    * Exclude the heritage items which this current user created.
                    * Returns heritage items, distinctly!
                """
                serializer = HeritageSerializer(Heritage.objects.all().filter(tags__name__in=tags_upvoted_items).exclude(creator=profile_id).distinct().order_by('id'), context=context, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_all_recommendations_tag_upvote_related(request):
    names_of_heritage_tags = []
    vote_heritage_tags = []
    if request.method == 'GET':
        try:
            context = {}
            if request.user.username:
                print request.user.username
                profile_id = Profile.objects.filter(username=request.user.username).first().pk
                heritage_tags = Heritage.objects.filter(creator=profile_id)
                # Take only UP votes
                votes_include_heritages = Vote.objects.filter(voter=profile_id, value=True)
                context['requester_profile_id'] = profile_id

                for v in votes_include_heritages:
                    vote_heritage_tags.append(v.heritage)


                for h in heritage_tags:
                    for t in h.tags.all():
                        names_of_heritage_tags.append(t.name)

                for h in vote_heritage_tags:
                    for t in h.tags.all():
                        names_of_heritage_tags.append(t.name)
                names_of_heritage_tags = list(set(names_of_heritage_tags))

                serializer = HeritageSerializer(Heritage.objects.all().
                                                filter(tags__name__in=names_of_heritage_tags).
                                                exclude(creator=profile_id).distinct(), context=context, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)





