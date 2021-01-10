# -*- coding:utf-8 -*-

"""Test for function generating difference."""

import pytest
import json
from gendiff.comparator import generate_diff

# showing which files used for testcases


path_to_fixtures = 'tests/fixtures/'


cases = [
    (
        path_to_fixtures + 'before.json',
        path_to_fixtures + 'after.json',
        'stylish',
        path_to_fixtures + 'expected_stylish.txt'
    ),
    (
        path_to_fixtures + 'before.yaml',
        path_to_fixtures + 'after.yaml',
        'plain',
        path_to_fixtures + 'expected_plain.txt'
    ),
    (
        path_to_fixtures + 'before.json',
        path_to_fixtures + 'after.json',
        'json',
        path_to_fixtures + 'expected_json.json'
    )]


@pytest.mark.parametrize('path_to_first, path_to_second, form, expected', cases)
def test_generate_diff(path_to_first, path_to_second, form, expected):
    with open(expected, 'r') as file:
        if form == 'json':
            assert json.load(file) == json.loads(generate_diff(path_to_first, path_to_second, form))
        else:
            assert file.read() == generate_diff(path_to_first, path_to_second, form)
