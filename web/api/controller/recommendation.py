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
from api.controller.heritage import get_trending_heritages
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

    max = 0
    max_val =0
    for key,value in recommended_items.items():
        if value>max_val:
            max_val=value
            max = key
        #print (key,value)
    sorted_rec_items = (sorted(recommended_items, key=recommended_items.get))[::-1] #reverse sort the list

    #print 'sorted keys'
    #print sorted_rec_items

    #recommend only 7 items if more than 7 items are returned
    if sorted_rec_items.__sizeof__()>7:
        sorted_rec_items = sorted_rec_items[:7]
    response_items = []
    for heritage_id in sorted_rec_items:
        response_items.append(Heritage.objects.get(id=heritage_id))

    if request.user.is_authenticated:
        context = {}
        profile_id = Profile.objects.filter(username=request.user.username).first().pk
        context['requester_profile_id'] = profile_id

        serializer = HeritageSerializer(response_items, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = HeritageSerializer(response_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def user_based_alternative(request):

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

        sorted_res = recommendation.alternative_recommendation_for_heritage(item)

        for item_id, score in sorted_res:
            if item_id in res.keys():
                res[item_id] += score
            else:
                res[item_id] = score
    #sort res
    sorted_res = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    sorted_keys = [x[0] for x in sorted_res]

    print sorted_res

    if len(sorted_res)==0:
        return get_trending_heritages(request)

    response=[]
    count = 5
    for item in sorted_keys:
        if count > 0 and item not in exclude_ids:
            heritage_item = Heritage.objects.get(id=item)
            #print heritage_item
            serializer = HeritageSerializer(heritage_item)
            response.append(serializer.data)
            count-=1


    return Response(response, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def heritage_based_alternative(request, item_id):

    the_heritage = Heritage.objects.get(id=item_id)
    sorted_res = recommendation.alternative_recommendation_for_heritage(the_heritage)
    sorted_keys = [x[0] for x in sorted_res]


    response_items = []
    count = 5
    for item in sorted_keys:
        if count > 0:
            heritage_item = Heritage.objects.get(id=item)
            response_items.append(heritage_item)
            count-=1

    if request.user.is_authenticated:
        context = {}
        profile_id = Profile.objects.filter(username=request.user.username).first().pk
        context['requester_profile_id'] = profile_id

        serializer = HeritageSerializer(response_items, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = HeritageSerializer(response_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)