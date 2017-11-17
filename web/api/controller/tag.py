from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.model.profile import Profile
from api.model.tag import Tag
from api.model.heritage import Heritage
from api.serializer.tag import TagSerializer
from api.serializer.heritage import HeritageSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_tag_to_existed_heritage_item(request):
    """
    CURRENTLY NOT WORKING,
    is_tag_exist: whether tag is exist in DB or not.
    is_tag_exist = Tag.objects.filter(tag_name=request.data['name']).exists()

    if is_tag_exist:
        #fcerfvdf
    else:
        serializer = TagSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """


@api_view(['GET'])
@permission_classes((AllowAny, ))
def list_all_tags(request):
    try:
        serializer = TagSerializer(Tag.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_all_heritage_items_own_this_tag(request, tag_id):
    try:
        heritage = Heritage.objects.get(tags__id=tag_id)
        serializer = HeritageSerializer(heritage)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
