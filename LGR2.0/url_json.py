import requests as requests
import json5


def url_json(url):
    # print(url)
    json = requests.get(url)
    # print(json.text)
    obj = json5.loads(json.text)
    # print(url)
    # print(obj)
    return obj
