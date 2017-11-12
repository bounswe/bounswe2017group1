from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Heritage
from api.serializer.heritage import HeritageSerializer
from api.service import search


@api_view(['GET'])
def basic_search(request):
    query = request.GET.get('query')
    search.get_items_by_location(location=query)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def advanced_search(request):
    print request.data
    return Response(status=status.HTTP_200_OK)