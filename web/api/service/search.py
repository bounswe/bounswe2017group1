from rest_framework import status
from rest_framework.response import Response

from api.models import Heritage
from api.serializer.heritage import HeritageSerializer


def get_items_by_location(location):
    items = Heritage.objects.filter(location__istartswith=location)
    response_data = {}

    for item in items:
        print item


def get_items_by_tag(tag):
    items = Heritage.objects.filter(tag__icontains=tag)
    print items


def get_items_by_title(title):
    items = Heritage.objects.filter(title__icontains=title)
    print items


def get_items_by_creator(creator):
    items = Heritage.objects.filter(creator__user__username__istartswith=creator)
    print items