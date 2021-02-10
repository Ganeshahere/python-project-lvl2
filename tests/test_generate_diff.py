import pytest
from json import loads
from os.path import abspath
from gendiff import generate_diff, load


json_before = abspath('tests/fixtures/before.json')
json_after = abspath('tests/fixtures/after.json')

yaml_before = abspath('tests/fixtures/before.yaml')
yaml_after = abspath('tests/fixtures/after.yaml')

complex_json_before = abspath('tests/fixtures/complex_before.json')
complex_json_after = abspath('tests/fixtures/complex_after.json')

complex_yaml_before = abspath('tests/fixtures/complex_before.yaml')
complex_yaml_after = abspath('tests/fixtures/complex_after.yaml')

simple_diff = open(abspath('tests/fixtures/simple_diff.txt')).read()
stylish_diff = open(abspath('tests/fixtures/stylish_diff.txt')).read()
plain_diff = open(abspath('tests/fixtures/plain_diff.txt')).read()
json_diff = load('tests/fixtures/json_diff.json')


@pytest.mark.parametrize(
    "before, after, render, expected", [
        (json_before, json_after, 'stylish', simple_diff),
        (yaml_before, yaml_after, 'stylish', simple_diff),  # noqa: E501
        (complex_json_before, complex_json_after, 'plain', plain_diff),
        (complex_yaml_before, complex_yaml_after, 'plain', plain_diff),
    ]
)
def test_generate_diff(before, after, render, expected):
    assert generate_diff(before, after, render) == expected


@pytest.mark.parametrize(
    "before, after, render, expected", [
        (complex_json_before, complex_json_after, 'json', json_diff),
        (complex_yaml_before, complex_yaml_after, 'json', json_diff),
    ]
)
def test_generate_json_diff(before, after, render, expected):
    assert loads(generate_diff(before, after, render)) == expected
