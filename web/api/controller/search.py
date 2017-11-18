from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from api.models import Heritage
from api.serializer.heritage import HeritageSerializer
from api.service import search, heritage

def consecutive_subsequences(iterable):

    ret = []
    for length in range(len(iterable)):
        for i in range(len(iterable) - length):
            l = iterable[i: i+length+1]
            ret.append(" ".join(l))

    return ret


@api_view(['POST'])
@permission_classes((AllowAny, ))
def search(request):
    query_words = request.data('query').split(' ')
    filters = request.data('filters', None)
    query_combinations = consecutive_subsequences(query_words)

    ll = {}

    for index in range(len(query_combinations)):
        #print search.get_items_by_tag(tag=query_combinations[index])
        score_list = search.calculate_scores(query_combinations[index], filters)

        for iter in score_list:
            if iter[0] in ll.keys():
                ll[iter[0]] += iter[1]
            else:
                ll[iter[0]] = iter[1]

    print ll

    response = []

    for id in ll.keys():
        heritage_item = heritage.get_item_by_id(heritage_id=id)
        serializer = HeritageSerializer(heritage_item)
        response.append(serializer.data)
    #return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(response, status=status.HTTP_200_OK)

