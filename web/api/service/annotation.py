

import requests, json
import sys


def create_annotation(body, target):
    """
    create an annotation with given body and target
    to do this, make request to annotation server

    :param body: text of annotation
    :param target: indicates which item and its field make annotation on and annotation coordinates
    :return: status_code of response
    """
    data = {
        "@context": "http://www.w3.org/ns/oa.jsonld",
        "@type": "oa:Annotation",
        "body": body,
        "target": target
    }

    header = {"Content-Type": "application/ld+json"}

    r = requests.post("http://127.0.0.1:8000/annotations/", headers=header, data=json.dumps(data))
    return r.status_code


def pretty(data):
    """
    make the response pretty

    :param data: json data
    """
    doc = json.loads(data)
    print(json.dumps(doc, sort_keys=True, indent=2, separators=(',', ': ')))


def get_all_annotations():
    """
    get all annotations
    to do this, make request to annotation server

    :return: list of all annotations
    """
    header = {"Content-Type": "application/ld+json"}

    r = requests.get("http://127.0.0.1:8000/annotations/", headers=header)

    return json.loads(r.text)

def get_annotations_of_item_id(item_id):
    """
    get all annotations of the indicated heritage item

    :param item_id: indicates the heritage item
    :return: list of all annotations of the indicated heritage item
    """
    annotations_of_item = {}
    pattern = "heritage/"+item_id
    all_annotations = get_all_annotations()
    #all_annotations_graph = all_annotations.pop('@graph', None)
    annotations_of_item = []

    for anno in all_annotations['@graph']:
        if pattern in anno['target']:
            annotations_of_item.append(anno)

    return annotations_of_item