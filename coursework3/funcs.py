import json
from os.path import abspath
from datetime import datetime


def json_to_list(path=abspath('../data/operations.json')):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data


def correct_data(data):
    correct = []
    for obj in data:
        if obj and obj.get('date') is not None and obj.get('state') == 'EXECUTED':
            obj['date'] = datetime.fromisoformat(obj['date'])
            correct.append(obj)
    return correct


def five_operations(data):
    new_data = sorted(data, key=lambda x: x['date'], reverse=True)[:5]
    return new_data


def dt_to_str(dt):
    pattern = '%d.%m.%Y'
    return dt.strftime(pattern)


