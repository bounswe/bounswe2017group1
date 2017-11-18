from rest_framework import status
from rest_framework.response import Response

from api.models import Heritage
from api.serializer.heritage import HeritageSerializer

from api.service import heritage

import re
import operator

TITLE_COEF = 5
DESC_COEF = 3
LOC_COEF = 3
TAG_COEF = 5

def calculate_scores(word):

    scores = {}

    items = Heritage.objects.all()

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