# -*- coding:utf-8 -*-

"""Test for function generating difference."""

import pytest
from gendiff.comparator import generate_diff

# showing which files used for testcases
DATA_SET_FOR_TESTCASES = {
    'complex_json': 'complex_json_files',
    'format_json': 'complex_json_files',
    'format_plain': 'complex_json_files'
}

# paths for input files
DATA_SET_PATHS = {
    'complex_json_files': (
        'tests/fixtures/before.json',
        'tests/fixtures/after.json',
    ),
    'plain_yaml_files': (
        'tests/fixtures/before.yaml',
        'tests/fixtures/after.yaml'),
}

# paths for expected files for each testcase
EXPECTED_RESULTS_PATHS = {
    'complex_json': 'tests/fixtures/expected_stylish.txt',
    'format_plain': 'tests/fixtures/expected_plain.txt',
    'format_json': 'tests/fixtures/expected_json.json'
}


@pytest.fixture()
def expected_results():
    def get_expected_result(testcase):
        filepath = EXPECTED_RESULTS_PATHS[testcase]
        with open(filepath) as file:
            return file.read()

    return get_expected_result


@pytest.fixture()
def data_sets():
    def get_filepaths(testcase):
        data_set = DATA_SET_FOR_TESTCASES[testcase]
        return DATA_SET_PATHS[data_set]
    return get_filepaths


def test_complex_json(data_sets, expected_results):
    testcase = 'complex_json'
    format = 'stylish'
    first, second = data_sets(testcase)
    assert expected_results(testcase) == generate_diff(first, second, format)


def test_format_plain(data_sets, expected_results):
    testcase = 'format_plain'
    format = 'plain'
    first, second = data_sets(testcase)
    assert expected_results(testcase) == generate_diff(first, second, format)


def test_format_json(data_sets, expected_results):
    testcase = 'format_json'
    format = 'json'
    first, second = data_sets(testcase)
    assert expected_results(testcase) == generate_diff(first, second, format)
