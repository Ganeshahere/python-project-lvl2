# -*- coding: utf-8 -*-


"""Functions to build difference."""

from gendiff import formatters, parsers
from gendiff.nodetypes import ADDED, CHANGED, PARENT, REMOVED, UNCHANGED


def diff_dict(dict1, dict2):
    """Difference between first and second dicts."""
    first_keys = dict1.keys()
    second_keys = dict2.keys()

    add_keys = second_keys - first_keys
    remove_keys = first_keys - second_keys
    common_keys = first_keys & second_keys

    added = {
        key: {'type': ADDED, 'value': dict2[key]}
        for key in add_keys
    }
    removed = {
        key: {'type': REMOVED, 'value': dict1[key]}
        for key in remove_keys
    }

    common = {}
    for key in common_keys:
        if dict1[key] == dict2[key]:
            common[key] = {
                'type': UNCHANGED,
                'value': dict2[key],
            }
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            common[key] = {
                'type': PARENT,
                'children': diff_dict(dict1[key], dict2[key]),
            }
        else:
            common[key] = {
                'type': CHANGED,
                'value': dict2[key],
                'oldValue': dict1[key],
            }

    return {**common, **added, **removed}


def generate_diff(path_to_file1: str, path_to_file2: str):
    """Generate message of difference between fwo files."""
    with open(path_to_file1) as first_file:
        first_data = parsers.parse(
            _format_data(path_to_file1),
            first_file.read(),
        )
    with open(path_to_file2) as second_file:
        second_data = parsers.parse(
            _format_data(path_to_file2),
            second_file.read(),
        )
    diff = diff_dict(first_data, second_data)
    return renderers.build(diff)


def _format_data(path_to_file):
    return path_to_file.split('.')[-1]
