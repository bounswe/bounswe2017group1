"""
    This controller handles the routing for heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.model.profile import Profile




from api.model.heritage import Heritage
from api.serializer.heritage import HeritageSerializer


@api_view(['POST'])
def heritage_post(request):
    serializer = HeritageSerializer(data=request.data)

    username = request.user.username
    request.data['creator'] = Profile.objects.filter(username=username).first().pk
    request.data['creator'] = Profile.objects.filter(username=username).first().pk


    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def heritage_get_first(request):
    try:
        heritage = Heritage.objects.first()
        print(heritage.creator)
        serializer = HeritageSerializer(heritage)
        return Response(serializer.data)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
def heritage_get_put_delete(request,pk):
    try:
        heritage = Heritage.objects.get(id=pk)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HeritageSerializer(heritage)
        return Response(serializer.data)

    elif request.method == 'PUT':
        username = request.user.username
        request.data['creator'] = Profile.objects.filter(username=username).first().pk

        serializer = HeritageSerializer(instance=heritage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        heritage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def heritage_get_all(request):
    try:
        serializer = HeritageSerializer(Heritage.objects.all(), many=True)
        return Response(serializer.data)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

