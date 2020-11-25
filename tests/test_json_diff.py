# -*- coding: utf-* -*-

"""JSON files diff test."""

import pytest

from gendiff.comparator import diff_dict, generate_diff
from gendiff.nodetypes import ADDED, CHANGED, PARENT, REMOVED, UNCHANGED


def test_diff_dict():
    first = {
        'common': {
            'setting1': 'Value 1',
            'setting2': '200',
            'setting3': True,
            'setting6': {
                'key': 'value',
            },
        },
        'group1': {
            'baz': 'bas',
            'foo': 'bar',
        },
        'group2': {
            'abc': '12345',
        },
        'test': 'test',
        'foo': 'bar',
    }
    second = {
        'common': {
            'setting1': 'Value 1',
            'setting3': True,
            'setting4': 'blah blah',
            'setting5': {
                'key5': 'value5',
            },
        },
        'group1': {
            'foo': 'bar',
            'baz': 'bars',
        },
        'group3': {
            'fee': '100500',
        },
        'test': 'test',
        'foo': 'baz',
    }
    diff = diff_dict(first, second)

    assert diff == {
        'common': {
            'type': PARENT,
            'children': {
                'setting1': {
                    'type': UNCHANGED,
                    'value': 'Value 1',
                },
                'setting2': {
                    'type': REMOVED,
                    'value': '200',
                },
                'setting3': {
                    'type': UNCHANGED,
                    'value': True,
                },
                'setting4': {
                    'type': ADDED,
                    'value': 'blah blah',
                },
                'setting5': {
                    'type': ADDED,
                    'value': {'key5': 'value5'},
                },
                'setting6': {
                    'type': REMOVED,
                    'value': {'key': 'value'},
                },
            },
        },
        'group1': {
            'type': PARENT,
            'children': {
                'baz': {
                    'type': CHANGED,
                    'value': 'bars',
                    'oldValue': 'bas',
                },
                'foo': {'type': UNCHANGED, 'value': 'bar'},
            },
        },
        'group2': {
            'type': REMOVED,
            'value': {'abc': '12345'},
        },
        'group3': {
            'type': ADDED,
            'value': {'fee': '100500'},
        },
        'test': {'type': UNCHANGED, 'value': 'test'},
        'foo': {'type': CHANGED, 'value': 'baz', 'oldValue': 'bar'},
    }


def test_text_json_diff(expected_text_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_result='text',
    )
    assert diff.split('\n') == expected_text_result


def test_yaml_diff(expected_text_result):
    diff = generate_diff(
        'tests/fixtures/before.yaml',
        'tests/fixtures/after.yaml',
        format_result='text',
    )
    assert diff.split('\n') == expected_text_result


def test_json_yaml_diff(expected_text_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.yaml',
        format_result='text',
    )
    assert diff.split('\n') == expected_text_result


def test_build_json_diff(expected_build_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_result='build',
    )
    assert sorted(diff.split('\n')) == sorted(expected_build_result)


@pytest.fixture
def expected_text_result():
    with open('tests/fixtures/expected_text.txt') as file:
        yield file.read().splitlines()


@pytest.fixture
def expected_build_result():
    with open('tests/fixtures/expected_build.txt') as file:
        yield file.read().splitlines()
