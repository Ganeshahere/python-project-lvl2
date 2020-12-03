# -*- coding: utf-8 -*-

"""JSON files diff test."""

import pytest
import json

from gendiff.comparator import generate_diff


def test_text_json_diff(expected_stylish_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_result='stylish',
    )
    assert diff.split('\n') == expected_stylish_result


def test_yaml_diff(expected_stylish_result):
    diff = generate_diff(
        'tests/fixtures/before.yaml',
        'tests/fixtures/after.yaml',
        format_result='stylish',
    )
    assert diff.split('\n') == expected_stylish_result


def test_json_yaml_diff(expected_stylish_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.yaml',
        format_result='stylish',
    )
    assert diff.split('\n') == expected_stylish_result


def test_plain_format(expected_plain_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_result='plain',
    )
    assert sorted(diff.split('\n')) == sorted(expected_plain_result)


def test_json_format(expected_json_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_result='json',
    )
    assert json.loads(diff) == expected_json_result


@pytest.fixture
def expected_stylish_result():
    with open('tests/fixtures/expected_stylish.txt') as file:
        yield file.read().splitlines()


@pytest.fixture
def expected_plain_result():
    with open('tests/fixtures/expected_plain.txt') as file:
        yield file.read().splitlines()


@pytest.fixture
def expected_json_result():
    with open('tests/fixtures/expected_json.json') as file:
        yield json.load(file)
