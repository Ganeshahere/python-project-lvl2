# -*- coding: utf-8 -*-


"""Functions to build difference."""

from gendiff import formatters, parsers


def diff_dict(dict1, dict2):
    """Difference between first and second dicts."""
    first_keys = dict1.keys()
    second_keys = dict2.keys()

    add_keys = second_keys - first_keys
    remove_keys = first_keys - second_keys
    common_keys = first_keys & second_keys

    added = {key: dict2[key] for key in add_keys},
    removed = {key: dict1[key] for key in remove_keys},
    changed = {
        key: {'old': dict1[key], 'new': dict2[key]}
        for key in common_keys
        if dict1[key] != dict2[key]
    }
    unchanged = {
        key: dict1[key] for key in common_keys if dict1[key] == dict2[key]
    }
    return {
        'added': added,
        'removed': removed,
        'changed': changed,
        'unchanged': unchanged,
    }


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
    return formatters.build_message(diff)


def _format_data(path_to_file):
    return path_to_file.split('.')[-1]
