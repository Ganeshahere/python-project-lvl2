# -*- coding:utf-8 -*-

"""Test for function generating difference."""

import pytest
import json
import os
import pathlib
from gendiff import parsers
from gendiff.formatters import formatter
from gendiff.comparator import generate_diff

# showing which files used for testcases


path_to_fixtures = 'tests/fixtures/'
FIXTURES_DIR = 'fixtures'
formats = {
    "json": "json",
    "yml": "yml",
    "yaml": "yaml"
}
output_formats = {
    "plain": "plain",
    "stylish": "stylish",
    "json": "json"
}


def get_path(file_name):
    dir_path = pathlib.Path(__file__).absolute().parent
    return os.path.join(dir_path, FIXTURES_DIR, file_name)


def read_file(path):
    with open(path) as f:
        result = f.read()
    return result


map_format_to_result = {}
for format in output_formats:
    map_format_to_result[format] = read_file(
        get_path(f'result.{format}')
    )

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


@pytest.mark.parametrize('format', formats)
def test_gendiff_format(format):
    """checking that format is working right."""
    file_path_1 = get_path(f'before.{format}')
    file_path_2 = get_path(f'after.{format}')
    for output_format in output_formats:
        diff = generate_diff(file_path_1, file_path_2, output_format)

        if output_format == formats["json"]:
            json_result = map_format_to_result[output_format]
            assert json.loads(diff) == json.loads(json_result)
            continue
        assert diff == map_format_to_result[output_format]


def test_gendiff_default():
    """Checking default format"""
    file_path_1 = get_path('before.json')
    file_path_2 = get_path('after.yml')
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == map_format_to_result['stylish']
