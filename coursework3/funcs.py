import json
from os.path import abspath
from datetime import datetime


def json_to_list(path=abspath('../data/operations.json')):
    """Дессериалиации json"""
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    return data


def correct_data(data):
    """Проверка корректности данных,
    удаление пустых строк, оставляем записи со статусом EXECUTE,
    преобразование дат в тип datetime"""
    correct = []
    for obj in data:
        if obj and obj.get('date') is not None and obj.get('state') == 'EXECUTED':
            obj['date'] = datetime.fromisoformat(obj['date'])
            correct.append(obj)
    return correct


def five_operations(data):
    """Сортировка данных по убыванию дат, оставляем только 5 первыхаписей"""
    new_data = sorted(data, key=lambda x: x['date'], reverse=True)[:5]
    return new_data


def dt_to_str(dt):
    """Преобразование типов datetime в формат ДД.ММ.ГГГГ """
    pattern = '%d.%m.%Y'
    return dt.strftime(pattern)

