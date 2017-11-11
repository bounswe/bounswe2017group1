from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Heritage
from api.serializer.heritage import HeritageSerializer

@api_view(['GET'])
def searchItemByLocation(request, location):
    items = Heritage.objects.filter(location__istartswith=location)

    response_data = {}

    for item in items:
        print item.tags.name

    return Response(response_data, status=status.HTTP_200_OK)

def searchItemByTag(request, tag):
    items = Heritage.objects.filter(tag__icontains=tag)
    print items

def searchItemByTitle(request, title):
    items = Heritage.objects.filter(title__icontains=title)
    print items

def searchItemByCreator(request, creator):
    items = Heritage.objects.filter(creator__user__username__istartswith=creator)
    print items