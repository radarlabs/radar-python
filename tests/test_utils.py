import pytest
from unittest.mock import patch, Mock

from radar.utils import remove_none_values, obj_to_dict


class Dummy:
    def __init__(self, num, arr, string, nested_dict):
        self.num = num
        self.arr = arr
        self.string = string
        self.nested_dict = nested_dict


def test_obj_to_dict():
    dummy_obj = Dummy(
        num=5,
        arr=[1, 2, 3, 4],
        string="radar string",
        nested_dict={"level1": {"level2": "val"}},
    )
    dictionary = obj_to_dict(dummy_obj)

    assert type(dummy_obj) is not dict
    assert type(dictionary) is dict
    assert dictionary["num"] == dummy_obj.num
    assert dictionary["arr"] == dummy_obj.arr
    assert dictionary["string"] == dummy_obj.string
    assert dictionary["nested_dict"] == dummy_obj.nested_dict
    assert dictionary["nested_dict"]["level1"]["level2"] == "val"


def test_remove_none_values():
    params = {
        "name": None,
        "coordinates": [12.3456, -78.90],
        "createdBefore": None,
        "limit": 100,
    }
    query = remove_none_values(params)

    for key, value in query.items():
        assert value is not None

    assert "name" not in query
    assert "coordinates" in query
    assert "createdBefore" not in query
    assert "limit" in query
