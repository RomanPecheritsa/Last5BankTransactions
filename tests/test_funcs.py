import pytest
from datetime import datetime
from coursework3.funcs import correct_data, json_to_list


@pytest.mark.parametrize('list_dict, expected', [
    ([{}], []),
    ([{"date": "2019-04-04T23:20:05.206878", "state": "EXECUTED"}],
     [{"date": datetime.fromisoformat("2019-04-04T23:20:05.206878"), "state": "EXECUTED"}]),
    ([{"date": "2019-04-04T23:20:05.206878"}], []),
    ([{"state": "EXECUTED"}], []),
])
def test_correct_data(list_dict, expected):
    assert correct_data(list_dict) == expected


def test_json_to_list():
    with pytest.raises(FileNotFoundError):
        json_to_list('egegeg/error.txt')