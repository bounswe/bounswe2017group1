import json

from api.model.heritage import Heritage
from api.model.comment import Comment
from api.model.tag import Tag
from api.serializer.comment import CommentSerializer
from api.serializer.tag import TagSerializer

def get_item_by_id(heritage_id):
        return Heritage.objects.get(id=heritage_id)

def get_all_comments(heritage_id):
    comments = Comment.objects.all().filter(heritage=heritage_id)

    ret = []
    for comment in comments:
        serializer = CommentSerializer(comment)
        ret.append(serializer.data)

    return ret

def get_all_tags(heritage_id):
    tags = Tag.objects.filter(heritage_id=heritage_id)

    ret = []
    for tag in tags:
        serializer = TagSerializer(tag)
        ret.append(serializer.data)

    return ret

