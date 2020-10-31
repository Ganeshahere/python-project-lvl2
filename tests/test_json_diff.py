# -*- coding: utf-* -*-

"""JSON files diff test."""

import pytest

from gendiff.comparator import diff_dict, generate_diff


def test_dict_diff():
    first = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22'}
    second = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    difference = diff_dict(first, second)

    assert diff == {
        'added': {'verbose': True},
        'removed': {'proxy': '123.234.53.22'},
        'changed': {'timeout': {'new': 20, 'old': 50}},
        'unchanged': {'host': 'hexlet.io'},
    }


def test_json_difference(expected_message):
    difference = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json'
    )
    assert difference.split('\n') == expected_message


def test_yaml_difference(expected_message):
    difference = generate_diff(
        'tests/fixtures/before.yaml',
        'tests/fixtures/after.yaml',
    )
    assert difference.split('\n') == expected_message


def test_json_yaml_diff(expected_message):
    difference = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.yaml',
    )
    assert difference.split('\n') == expected_message


@pytest.fixture
def expected_message(request):
    with open('tests/fixtures/expected_message.txt') as file:
        yield file.read().splitlines()
