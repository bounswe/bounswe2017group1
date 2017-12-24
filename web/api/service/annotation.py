import requests, json

def post_annotation(body, target):

    data = {
        "@context": "http://www.w3.org/ns/oa.jsonld",
        "@type": "oa:Annotation",
        "body": body,
        "target": target
    }

    header = {"Content-Type": "application/ld+json"}

    r = requests.post("http://127.0.0.1:8000/annotations/", headers=header, data=json.dumps(data))
    return r.status_code