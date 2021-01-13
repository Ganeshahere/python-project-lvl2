# -*- coding: utf-8 -*-


"""Functions to build difference."""

from gendiff import formatters
from gendiff.parsers import get_parsed_data
from gendiff.constants import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED


def diff_dict(first, second):
    """Diff between first and second dicts."""
    first_keys = first.keys()
    second_keys = second.keys()

    add_keys = second_keys - first_keys
    remove_keys = first_keys - second_keys
    common_keys = first_keys & second_keys

    added = {
        key: {'type': ADDED, 'value': second[key]}
        for key in add_keys
    }
    removed = {
        key: {'type': REMOVED, 'value': first[key]}
        for key in remove_keys
    }

    common = {}
    for key in common_keys:
        if first[key] == second[key]:
            common[key] = {
                'type': UNCHANGED,
                'value': second[key],
            }
        elif isinstance(first[key], dict) and isinstance(second[key], dict):
            common[key] = {
                'type': NESTED,
                'children': diff_dict(first[key], second[key]),
            }
        else:
            common[key] = {
                'type': CHANGED,
                'value': second[key],
                'oldValue': first[key],
            }

    return {**common, **added, **removed}


def generate_diff(path_to_file1: str, path_to_file2: str, format_result: str):
    """Generate message different two files."""
    first_data = get_parsed_data(path_to_file1)
    second_data = get_parsed_data(path_to_file2)
    diff = diff_dict(first_data, second_data)
    return formatters.format_ast(diff, format_result)


def _format_data(path_to_file):
    return path_to_file.split('.')[-1]
