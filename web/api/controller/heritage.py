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
    print "\n--- ",request.user," \n"
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


@api_view(['GET'])
def heritage_get(request,pk):
    try:
        heritage = Heritage.objects.get(id=pk)
        print(heritage.creator)
        serializer = HeritageSerializer(heritage)
        return Response(serializer.data)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def heritage_get_all(request):
    try:
        serializer = HeritageSerializer(Heritage.objects.all(), many=True)
        return Response(serializer.data)
    except Heritage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

