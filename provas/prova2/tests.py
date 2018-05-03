import pytest
from datetime import date
try:
    from json_plus_resposta import parse_json as load
except ImportError:
    from json_plus import parse_json as load


def test_parse_basic_json_examples():
    # Keywords
    assert load('true') is True
    assert load('false') is False
    assert load('null') is None

    # Atoms
    assert load('42') == 42.0
    assert load('-1') == -1.0
    assert load('+1') == 1.0
    assert load('3.14') == 3.14
    assert load('"foo"') == 'foo'


def test_parse_advanced_json_examples():
    assert load('{"foo": "bar"}') == {'foo': 'bar'}
    assert load('[1, 2, 3, 4]') == [1, 2, 3, 4]
    assert load('{"foo": [{}, [], {"value": "bar"}]}') == \
        {'foo': [{}, [], {'value': 'bar'}]}


def test_ignore_comments():
    assert load('// cmt\n42') == 42
    assert load('42 // cmt') == 42


def test_can_create_structures_without_commas():
    assert load('[1 2 3]') == [1, 2, 3]
    assert load('{"foo": "bar" "ham": "spam"}') == \
        {'foo': 'bar', 'ham': 'spam'}


def test_accept_trailing_comma():
    assert load('[1, 2, 3,]') == [1, 2, 3]
    assert load('{"foo": "bar", "ham": "spam",}') == \
        {'foo': 'bar', 'ham': 'spam'}


def test_reject_duplicated_commas():
    with pytest.raises(Exception):
        load('[1,,2]')
    with pytest.raises(Exception):
        load('[1,2,,]')
    with pytest.raises(Exception):
        load('{"foo": "bar",, "ham": "spam"}')


def test_keys_can_be_variable_names():
    assert load('{foo: "bar", ham: "spam",}') == \
        {'foo': 'bar', 'ham': 'spam'}


def test_keywords_can_be_keys():
    assert load('{true: 1, false: 0, null: -1}') == \
        {'true': 1, 'false': 0, 'null': -1}


def test_values_cannot_be_variable_names():
    with pytest.raises(Exception):
        load('{"foo": bar}')
    with pytest.raises(Exception):
        load('foo')
    with pytest.raises(Exception):
        load('foobar')


def test_accept_date_values():
    assert load('2000-10-01') == date(2000, 10, 1)
    assert load('[1999-09-10]') == [date(1999, 9, 10)]
    assert load('{"date": 0002-01-10}') == {'date': date(2, 1, 10)}


def test_reject_invalid_date_values():
    with pytest.raises(Exception):
        load('2000-1-01')

    with pytest.raises(Exception):
        load('2000-30-01')
