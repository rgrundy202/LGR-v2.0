import requests as requests
import json5


def url_json(url):
    json = requests.get(url)
    obj = json5.loads(json.text)
    return obj
