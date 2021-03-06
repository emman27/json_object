"""
Tests for the JSONObject package
"""
import json
import datetime
import pytest
from . import JSONObject, MissingKeyError, SchemaError


def test_exception_subclassing():
    assert isinstance(MissingKeyError(), KeyError)


def test_schema_generation():
    with pytest.raises(SchemaError):
        JSONObject('not a schema')
    with pytest.raises(SchemaError):
        JSONObject(1)
    JSONObject({})
    JSONObject([])


def test_basic_usage():
    schema = JSONObject({
        'my_key': str,
        'my_int_key': int,
        'my_bool_key': bool,
        'my_float_key': float
    })
    original = {
        'my_key': 'my_key',
        'my_int_key': 1,
        'my_bool_key': True,
        'my_float_key': 1.17
    }
    assert schema.loads(json.dumps(original)) == original


def test_type_casting_string():
    schema = JSONObject({
        'my_key': str,
        'my_int_key': str,
        'my_bool_key': str,
        'my_float_key': str
    })
    original = {
        'my_key': 'my_key',
        'my_int_key': 1,
        'my_bool_key': True,
        'my_float_key': 1.17
    }
    assert schema.loads(json.dumps(original)) == {
        'my_key': 'my_key',
        'my_int_key': '1',
        'my_bool_key': 'True',
        'my_float_key': '1.17'
    }


def test_type_casting_int():
    schema = JSONObject({
        'my_key': int,
        'my_int_key': int,
        'my_bool_key': int,
        'my_float_key': int
    })
    original = {
        'my_key': '123',
        'my_int_key': 1,
        'my_bool_key': True,
        'my_float_key': 1.17
    }
    assert schema.loads(json.dumps(original)) == {
        'my_key': 123,
        'my_int_key': 1,
        'my_bool_key': 1,
        'my_float_key': 1
    }


def test_zero_casting():
    schema = JSONObject({
        'my_key': str,
        'my_int_key': int,
        'my_bool_key': bool,
        'my_float_key': float
    })
    assert schema.loads(json.dumps({})) == {
        'my_key': '',
        'my_int_key': 0,
        'my_bool_key': False,
        'my_float_key': 0.0
    }


def test_nested_dic():
    schema = JSONObject({
        'dict_key': {
            'a': str,
            'second_dict': {
                'b': int,
                'c': list
            }
        }
    })
    assert schema.loads(json.dumps({})) == {
        'dict_key': {
            'a': '',
            'second_dict': {
                'b': 0,
                'c': []
            }
        }
    }


def test_strict_mode():
    schema = JSONObject({'a': str}, strict=True)
    with pytest.raises(MissingKeyError):
        schema.loads({})


def test_lists():
    schema = JSONObject([{'key': str}])
    dat = schema.loads([
        {'key': 1},
        {},
        {'key': 'a'},
        {'key': False}
    ])
    assert dat == [
        {'key': '1'},
        {'key': ''},
        {'key': 'a'},
        {'key': 'False'}
    ]


def test_dates():
    schema = JSONObject({
        'a': datetime.datetime,
        'b': datetime.datetime,
    })
    now = datetime.datetime.now()
    dat = schema.loads({
        'a': now.isoformat(),
    })
    assert dat == {
        'a': now,
        'b': None
    }
