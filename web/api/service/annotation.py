import requests, json
import sys


def create_annotation(body, target):

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
    doc = json.loads(data)
    print(json.dumps(doc, sort_keys=True, indent=2, separators=(',', ': ')))


def get_all_annotations():

    header = {"Content-Type": "application/ld+json"}

    r = requests.get("http://127.0.0.1:8000/annotations/", headers=header)

    return json.loads(r.text)

def get_annotations_of_item_id(item_id):

    annotations_of_item = {}
    pattern = "heritage/"+item_id
    all_annotations = get_all_annotations()
    #all_annotations_graph = all_annotations.pop('@graph', None)
    annotations_of_item['@graph'] = []

    for anno in all_annotations['@graph']:
        if pattern in anno['target']:
            annotations_of_item['@graph'].append(anno)

    return annotations_of_item