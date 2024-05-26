import json
from os.path import abspath
from datetime import datetime


def json_to_list(path=abspath('../data/operations.json')):
    """Дессериалиация json"""
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


def masked(source):
    """Маскировка счетов и карт"""
    def masked_account():
        """Маскировка счетов"""
        numb_account = '**' + numb[-4:]
        return numb_account

    def masked_card():
        """Маскировка карт"""
        numb_card = numb[:6] + ('*' * 6) + numb[-4:]
        numb_card = ' '.join(numb_card[i * 4:(i + 1) * 4] for i in range(4))
        return numb_card

    if source is None:
        return 'Unknown'

    *name, numb = source.split()
    if " ".join(name) == 'Счет':
        return f'Счет {masked_account()}'
    else:
        return f'{" ".join(name)} {masked_card()}'

