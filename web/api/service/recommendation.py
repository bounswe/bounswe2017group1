from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from api.model.tag import Tag
from api.model.vote import Vote
from api.model.heritage import Heritage
from api.model.profile import Profile
from api.serializer.heritage import HeritageSerializer
from api.service.search import calculate_scores
from api.service import heritage

from django.db.models import Prefetch
import operator
import re


def get_recommendation_for_heritage(heritage_obj):
    tags = heritage_obj.tags.all()
    query_words = []

    if heritage_obj.title:
        query_words.append(heritage_obj.title)

    if heritage_obj.location:
        pattern = re.compile("^\s+|\s*,\s*|\s+$")
        parsed_location = [x for x in pattern.split(heritage_obj.location) if x]
        query_words.extend(parsed_location)

    for tag in tags:
        #temporary solution to increase the weight of the tags
        query_words.append(tag.name)

        #print "tag: {}, related_list: {}".format(tag.name, tag.related_list)
        if tag.related_list is not None:
            tt = tag.related_list.split(' ')
            if tt[len(tt)-1] == '':
                tt = tt[:len(tt)-1]
            query_words.extend(tt)


    ll = {}

    for index in range(len(query_words)):
        # print search.get_items_by_tag(tag=query_combinations[index])
        score_list = calculate_scores(query_words[index], None)

        for iter in score_list:
            if iter[0] in ll.keys():
                ll[iter[0]] += iter[1]
            else:
                ll[iter[0]] = iter[1]

    del ll[heritage_obj.id]
    return ll


def mergeNListsWithoutDuplicate(listOfList, N):

    mergedSet = set(listOfList[0])
    for x in range(1, N):
        mergedSet |= set(listOfList[x])

    return list(mergedSet)


def matchScore(list1, list2, coef):
    matches = set(list1).intersection(list2)
    return (matches, len(matches)*coef)

TAG_TAG_COEF = 4
TAG_RELATED_COEF = 2
RELATED_TAG_COEF = 2
RELATED_RELATED_COEF = 1

LOCATION_LOCATION_COEF = 4

def alternative_recommendation_for_heritage(heritage_obj):
    toMerge = []

    """
        prepare needed lists of the item to search
    """
    item_tags = heritage_obj.tags.all()
    item_tags_names = []
    for tag in item_tags:
        item_tags_names.append(tag.name)
        related = tag.getlist()
        if related:
            toMerge.append(related)

    item_related_words = []
    if toMerge:
        item_related_words = mergeNListsWithoutDuplicate(toMerge, len(toMerge))

    item_location_words = heritage_obj.getLocationAsList()

    score = {}

    all_tags = Tag.objects.all()
    for tag in all_tags:

            """
                TAG - TAG Match
            """
            if tag.name in item_tags_names:
                #print tag.name
                items_match_tag_tag = tag.heritage_id.all().exclude(id=heritage_obj.id)

                if items_match_tag_tag:
                    for item in items_match_tag_tag:
                        if item.id in score.keys():
                            score[item.id] += TAG_TAG_COEF
                        else:
                            score[item.id] = TAG_TAG_COEF

            """
                TAG - RELATED Match
            """
            related = tag.getlist()
            if related and set(item_tags_names).intersection(related):
                #print tag.name
                items_match_tag_related = tag.heritage_id.all().exclude(id=heritage_obj.id)

                if items_match_tag_related:
                    for item in items_match_tag_related:
                        if item.id in score.keys():
                            score[item.id] += TAG_RELATED_COEF
                        else:
                            score[item.id] = TAG_RELATED_COEF

            """
                RELATED - TAG Match
            """
            if item_related_words and tag.name in item_related_words:
                # print tag.name
                items_match_related_tag = tag.heritage_id.all().exclude(id=heritage_obj.id)

                if items_match_related_tag:
                    for item in items_match_related_tag:
                        if item.id in score.keys():
                            score[item.id] += RELATED_TAG_COEF
                        else:
                            score[item.id] = RELATED_TAG_COEF

            """
                RELATED - RELATED Match
            """
            related = tag.getlist()
            if related and item_related_words and set(item_related_words).intersection(related):
                # print tag.name
                items_match_related_related = tag.heritage_id.all().exclude(id=heritage_obj.id)

                if items_match_related_related:
                    for item in items_match_related_related:
                        if item.id in score.keys():
                            score[item.id] += RELATED_RELATED_COEF
                        else:
                            score[item.id] = RELATED_RELATED_COEF


    """
        LOCATION - LOCATION Match
    """
    all_items = Heritage.objects.all()
    for item in all_items:
        if item.id != heritage_obj.id:
            location_words = item.getLocationAsList()
            if location_words and item_location_words:
                matches_count = len(set(item_location_words).intersection(location_words))
                if matches_count > 0:
                    if item.id in score.keys():
                        score[item.id] += matches_count * LOCATION_LOCATION_COEF
                    else:
                        score[item.id] = matches_count * LOCATION_LOCATION_COEF

    #print score
    sorted_score = sorted(score.items(), key=operator.itemgetter(1), reverse=True)
    #print sorted_score

    return sorted_score



