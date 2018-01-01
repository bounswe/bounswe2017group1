import json

from api.model.heritage import Heritage
from api.model.comment import Comment
from api.model.tag import Tag
from api.serializer.comment import CommentSerializer
from api.serializer.tag import ExtendedTagSerializer

def get_item_by_id(heritage_id):
    """
    get heritage item by id

    :param heritage_id: heritage item id
    :return: heritage item indicated by id
    """
    return Heritage.objects.get(id=heritage_id)

def get_all_comments(heritage_id):
    """
    get all comments of the heritage item

    :param heritage_id: indicates the heritage item
    :return: list of all comments of the heritage item indicated by id
    """
    comments = Comment.objects.all().filter(heritage=heritage_id)

    ret = []
    for comment in comments:
        serializer = CommentSerializer(comment)
        ret.append(serializer.data)

    return ret

def get_all_tags(heritage_id):
    """
    get all tags of the heritage item

    :param heritage_id: indicates the heritage item
    :return: list of all tags of the heritage item indicated by id
    """
    tags = Tag.objects.filter(heritage_id=heritage_id)

    ret = []
    for tag in tags:
        serializer = ExtendedTagSerializer(tag)
        ret.append(serializer.data)

    return ret

