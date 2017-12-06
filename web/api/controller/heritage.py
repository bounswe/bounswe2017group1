"""
    This controller handles the routing for heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from api.service import permission

from rest_framework.response import Response

from api.model.heritage import Heritage
from api.model.profile import Profile
from api.model.comment import Comment
from api.model.tag import Tag
from api.serializer.heritage import HeritageSerializer
from api.serializer.comment import CommentSerializer
from api.serializer.tag import TagSerializer

from api.service.heritage import get_all_comments, get_all_tags
from api.service import helper
import datetime


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def heritage_get_post(request):
    if request.method == 'GET':

        try:
            context = {}
            if request.user.username:
                profile_id = Profile.objects.filter(username=request.user.username).first().pk
                context['requester_profile_id'] = profile_id
            serializer = HeritageSerializer(Heritage.objects.all(),context=context, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Heritage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'POST' and request.user.is_authenticated:

        username = request.user.username
        profile_id = Profile.objects.filter(username=username).first().pk
        request.data['creator'] = profile_id
        context = {}
        context['requester_profile_id'] = profile_id

        serializer = HeritageSerializer(data=request.data,context=context)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def heritage_get_put_delete(request, heritage_id):
    try:
        context = {}
        if request.user.username:
            profile_id = Profile.objects.filter(username=request.user.username).first().pk
            context['requester_profile_id'] = profile_id
        heritage = Heritage.objects.get(id=heritage_id)

    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = HeritageSerializer(heritage,context = context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT' and permission.isOwner(request, obj=heritage):
        username = request.user.username
        request.data['creator'] = Profile.objects.filter(username=username).first().pk

        serializer = HeritageSerializer(instance=heritage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' and permission.isOwner(request, obj=heritage):
        try:
            heritage.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_412_PRECONDITION_FAILED)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_all_comments(request, heritage_id):
    comments = Comment.objects.all().filter(heritage=heritage_id)
    head_comments = comments.filter(parent_comment=None)
    ordered_comment_ids = []
    ordered_comments = []

    for comment in head_comments:
        ordered_comment_ids.append(comment.pk)
        for subcomment in comments.filter(parent_comment=comment.pk):
            ordered_comment_ids.append(subcomment.pk)

    ordered_comments = []
    for id in ordered_comment_ids:
        ordered_comments.append(comments.get(id=id))

    context = {}
    if request.user.username:
        profile_id = Profile.objects.filter(username=request.user.username).first().pk
        context['requester_profile_id'] = profile_id
    serializer = CommentSerializer(ordered_comments, context=context, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_all_tags(request, heritage_id):
    tags = Tag.objects.filter(heritage_id=heritage_id)
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_new_heritages(request):
    try:
        context = {}
        if request.user.username:
            profile_id = Profile.objects.filter(username=request.user.username).first().pk
            context['requester_profile_id'] = profile_id

        heritages = Heritage.objects.order_by('-creation_date')
        serializer = HeritageSerializer(heritages, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_top_heritages(request):
    try:
        context = {}
        if request.user.username:
            profile_id = Profile.objects.filter(username=request.user.username).first().pk
            context['requester_profile_id'] = profile_id

        heritages = Heritage.objects.all()
        myList = []
        for item in heritages:
            votes =  item.votes.all()
            score = votes.filter(value=True).count() - votes.filter(value=False).count()
            myList.append((item, score ))

        myList.sort(key=lambda tup: tup[1], reverse=True);
        sorted_heritages = [x[0] for x in myList]
        serializer = HeritageSerializer(sorted_heritages, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_trending_heritages(request):
    try:
        now = datetime.datetime.utcnow()+datetime.timedelta(hours=3)
        context = {}
        if request.user.username:
            profile_id = Profile.objects.filter(username=request.user.username).first().pk
            context['requester_profile_id'] = profile_id

        heritages = Heritage.objects.all()
        myList = []
        for item in heritages:
            votes = item.votes.filter(update_date__gte=now-datetime.timedelta(days=7))
            score = votes.filter(value=True).count() - votes.filter(value=False).count()
            myList.append((item, score ))

        myList.sort(key=lambda tup: tup[1], reverse=True);
        sorted_heritages = [x[0] for x in myList]
        serializer = HeritageSerializer(sorted_heritages, context=context, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)