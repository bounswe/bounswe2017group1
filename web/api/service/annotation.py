import requests

def post_annotation(body, target):

    data = {
        "@context": "http://www.w3.org/ns/oa.jsonld",
        "@type": "oa:Annotation",
        "body": body,
        "target": target
    }

    header = {"Content-Type": "application/ld+json"}

    r = requests.post("ec2-18-196-2-56.eu-central-1.compute.amazonaws.com:8000/annotations/", data=data, header=header)
    return r.status_code