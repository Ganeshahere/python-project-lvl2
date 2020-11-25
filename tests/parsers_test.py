# -*- coding:utf-8 -*-

import pytest

from gendiff import parsers


def test_json_parse():
    json_data = """
{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22"
}
"""
    expected = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
    }

    assert parsers.parse('json', json_data) == expected


def test_yaml_parse():
    yaml_data = """
        host: hexlet.io
        timeout: 50
        proxy: "123.234.53.22"
"""
    expected = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
    }

    assert parsers.parse('yaml', yaml_data) == expected
    assert parsers.parse('yml', yaml_data) == expected


def test_not_supported_format():
    with pytest.raises(AttributeError):
        parsers.parse('blablaformat', 'blabla')
