from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from api.model.vote import Vote
from api.model.heritage import Heritage
from api.model.profile import Profile
from api.model.comment import Comment
from api.serializer.heritage import HeritageSerializer
from api.service import recommendation
import operator


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def user_based(request):

    user_upvoted_heritages = []
    user_commented_heritages = []

    context = {}
    profile_id = Profile.objects.filter(username=request.user.username).first().pk
    context['requester_profile_id'] = profile_id

    # Get all heritage items user created
    user_created_heritages = Heritage.objects.filter(creator=profile_id)

    # Get all heritage items user upvoted
    user_votes = Vote.objects.filter(voter=profile_id, value=True)
    for vote in user_votes:
        user_upvoted_heritages.append(vote.heritage)

    # Get all heritage items user commented
    user_comments = Comment.objects.filter(creator=profile_id)
    for comment in user_comments:
        user_commented_heritages.append(comment.heritage)

    # Merge created, upvoted and commented items by the user into a list without duplicate
    recommended_related_items = list(set(user_created_heritages)|set(user_upvoted_heritages)|set(user_commented_heritages))

    exclude_ids = []
    res = {}

    # put recommended items into a function and get recommendations for that item
    for item in recommended_related_items:

        if item.id not in exclude_ids:
            exclude_ids.append(item.id)

        recommended_items = recommendation.get_recommendation_for_heritage(item)

        for key in recommended_items.keys():
            if key in res.keys():
                res[key] += recommended_items[key]
            else:
                res[key] = recommended_items[key]
    #sort res
    sorted_res = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    sorted_keys = [x[0] for x in sorted_res]

    response=[]
    for item in sorted_keys:
        if item not in exclude_ids:
            heritage_item = Heritage.objects.get(id=item)
            serializer = HeritageSerializer(heritage_item)
            response.append(serializer.data)

    return Response(response, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def heritage_based(request, item_id):

    the_heritage = Heritage.objects.get(id=item_id)
    recommended_items = recommendation.get_recommendation_for_heritage(the_heritage)
    #recommend only 5 items if more than 5 items are returned
    rec_keys = recommended_items.keys()
    if rec_keys.__sizeof__()>5:
        rec_keys = rec_keys[:5]
    response_items = Heritage.objects.all().filter(id__in=rec_keys)

    if request.user.is_authenticated:
        context = {}
        profile_id = Profile.objects.filter(username=request.user.username).first().pk
        context['requester_profile_id'] = profile_id

        serializer = HeritageSerializer(response_items, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = HeritageSerializer(response_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)