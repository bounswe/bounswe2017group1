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



def alternative_recommendation_for_heritage(heritage_obj):
    toMerge = []

    """
        prepare needed lists of the item to search
    """
    item_tags = heritage_obj.tags.all()
    item_tags_names = []
    for tag in item_tags:
        item_tags_names.append(tag.name)

    same_tags_items = Heritage.objects.all().\
        filter(tags__name__in=item_tags_names).\
        exclude(id=heritage_obj.id)

    print same_tags_items

    """
    for tag in item_tags:

        if tag.related_list is not None:
            tt = tag.related_list.split(' ')
            if tt[len(tt)-1] == '':
                tt = tt[:len(tt)-1]
            toMerge.append(tt)

    item_related_words = mergeNListsWithoutDuplicate(toMerge, len(toMerge))


    toMerge = []

    all_tags = Tag.objects.all()
    for tag in all_tags:
        if tag not in item_tags:

            if tag.related_list is not None:
                tt = tag.related_list.split(' ')
                if tt[len(tt)-1] == '':
                    tt = tt[:len(tt)-1]
                toMerge.append(tt)

    merged_related_words = mergeNListsWithoutDuplicate(toMerge, len(toMerge))
    """




