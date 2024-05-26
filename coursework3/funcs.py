import json
from os.path import abspath


def json_to_list(path=abspath('../data/operations.json')):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data

