from rest_framework import status
from rest_framework.response import Response

from api.models import Heritage, Profile
import datetime
from api.serializer.heritage import HeritageSerializer

from api.service import heritage

import re
import operator

TITLE_COEF = 5
DESC_COEF = 3
LOC_COEF = 3
TAG_COEF = 5

def calculate_scores(word, filters):

    scores = {}

    items = Heritage.objects.all()
    if filters is not None:
        if filters['location'] is not None:
            items.filter(location__icontains=filters['location'])
        if filters['creator'] is not None:
            usr = Profile.objects.get(username=filters['creator'])
            items.filter(creator=usr)
        if filters['creation_start'] is not None and filters['creation_end'] is not None:
            items.filter(creation_date__range=[filters['creation_start'], filters['creation_end']])
        elif filters['creation_start'] is not None:
            items.filter(creation_date__range=[filters['creation_start'], datetime.datetime.max])
        elif filters['creation_end'] is not None:
            items.filter(creation_date__range=[datetime.datetime.min, filters['creation_end']])

        if filters['event_start'] is not None and filters['event_end'] is not None:
            items.filter(event_date__range=[filters['event_start'], filters['event_end']])
        elif filters['event_start'] is not None:
            items.filter(creation_date__range=[filters['event_start'], datetime.datetime.max])
        elif filters['event_end'] is not None:
            items.filter(creation_date__range=[datetime.datetime.min, filters['event_end']])

    for item in items:
        score = 0
        score += TITLE_COEF * int((re.search(word, item.title, re.IGNORECASE)) is not None)
        score += DESC_COEF * int((re.search(word, item.description, re.IGNORECASE)) is not None)
        score += LOC_COEF * int((re.search(word, item.location, re.IGNORECASE)) is not None)
        tags = heritage.get_all_tags(item.id)
        for tag in tags:
            score += TAG_COEF * int((re.search(word, tag['name'], re.IGNORECASE)) is not None)

        if score > 0:
            scores[item.id] = score

    #print scores
    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return scores


def get_items_by_location(location):
    items = Heritage.objects.filter(location__istartswith=location)
    response_data = {}

    for item in items:
        print item


def get_items_by_tag(tag):
    items = Heritage.objects.filter(tags__name__icontains=tag)
    print items


def get_items_by_title(title):
    items = Heritage.objects.filter(title__icontains=title)
    print items


def get_items_by_creator(creator):
    items = Heritage.objects.filter(creator__user__username__istartswith=creator)
    print items