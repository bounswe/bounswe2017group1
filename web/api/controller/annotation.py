"""
    This controller handles the routing for annotations of heritage items
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from api.service.annotation import create_annotation, get_all_annotations, get_annotations_of_item_id

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_annotation_on_media(request, item_id, media_id):
    """
    create an annotation on the media file(image, video) of the heritage item

    :param request: client request
    :param item_id: indicates the heritage item
    :param media_id: indicates the media file of the heritage item
    :return: Response only status_code
    """

    body = request.data.get('text', None)
    fragment_selector = ','.join(map(str, request.data['coordinates']))
    target = "heritage/" + item_id + "/media/" + media_id
    target += "#xywh=" + fragment_selector

    print body, target

    response_code = create_annotation(body, target)
    return Response(status=response_code)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_annotation_on_comment(request, item_id, comment_id):
    """
    create an annotation on the comment of the heritage item

    :param request: client request
    :param item_id: indicates the heritage item
    :param comment_id: indicates the comment of the heritage item
    :return: Response only status_code
    """

    body = request.data.get('text', None)
    fragment_selector = ','.join(map(str, request.data['coordinates']))
    target = "heritage/" + item_id + "/comment/" + comment_id
    target += "#char=" + fragment_selector

    print body, target

    response_code = create_annotation(body, target)
    return Response(status=response_code)

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def create_on_description_or_get(request, item_id):
    """
    create an annotation on the description of the heritage item
    or
    get the annotation on the description of the heritage item

    :param request: client request
    :param item_id: indicates the heritage item
    :return: Response annotations list on the description of the heritage item
    :return: Response only status_code
    :rtype: JSONArray
    """


    if request.method == 'POST':

        body = request.data.get('text', None)
        fragment_selector = ','.join(map(str, request.data['coordinates']))
        target = "heritage/" + item_id + "/description"
        target += "#char=" + fragment_selector

        print body, target

        response_code = create_annotation(body, target)
        return Response(status=response_code)

    elif request.method == 'GET':
        response = get_annotations_of_item_id(item_id)
        return Response(response, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_all(request):
    """
    display all annotations

    :param request: client request
    :return: Response list of all annotations
    :rtype: JSONArray
    """

    all_anno = get_all_annotations()
    response = all_anno['@graph']
    return Response(response, status=status.HTTP_200_OK)