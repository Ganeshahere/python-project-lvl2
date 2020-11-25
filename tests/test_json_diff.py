# -*- coding: utf-8 -*-

"""JSON files diff test."""

import pytest
import json

from gendiff.comparator import generate_diff


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


def test_plain_format(expected_plain_result):
    diff = generate_diff(
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
        format_result='build',
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
def expected_text_result():
    with open('tests/fixtures/expected_text.txt') as file:
        yield file.read().splitlines()


@pytest.fixture
def expected_plain_result():
    with open('tests/fixtures/expected_build.txt') as file:
        yield file.read().splitlines()


@pytest.fixture
def expected_json_result():
    with open('tests/fixtures/expected_json.json') as file:
        yield json.load(file)
