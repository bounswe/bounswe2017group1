from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from django.db.models import Q

from api.model.vote import Vote
from api.model.heritage import Heritage
from api.model.profile import Profile
from api.serializer.heritage import HeritageSerializer
from api.service.search import calculate_scores
from api.service import heritage


def get_recommendation_for_heritage(heritage_obj):
    tags = heritage_obj.tags.all()
    query_words = []

    if heritage_obj.title != "":
        query_words.append(heritage_obj.title)

    if heritage_obj.location != "":
        query_words.append(heritage_obj.location)

    for tag in tags:
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
