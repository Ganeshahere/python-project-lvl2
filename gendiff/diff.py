from collections import OrderedDict
from gendiff.loading import load
from gendiff.formatters import RENDERERS


def build(old_dict, new_dict):
    diff_dict = {}

    old_keys = set(old_dict)
    new_keys = set(new_dict)

    added_keys = new_keys.difference(old_keys)
    for key in added_keys:
        diff_dict[key] = ('ADDED', new_dict[key])

    removed_keys = old_keys.difference(new_keys)
    for key in removed_keys:
        diff_dict[key] = ('REMOVED', old_dict[key])

    common_keys = old_keys.intersection(new_keys)
    for key in common_keys:
        old_value = old_dict[key]
        new_value = new_dict[key]
        children = isinstance(old_value, dict) and isinstance(new_value, dict)

        if children:
            diff_dict[key] = ('NESTED', build(old_value, new_value))
        elif old_value != new_value:
            diff_dict[key] = ('CHANGED', old_value, new_value)
        else:
            diff_dict[key] = ('UNCHANGED', old_value)

    return OrderedDict(sorted(diff_dict.items()))


def generate_diff(file_path_before, file_path_after, format_name='stylish'):
    old_file = load(file_path_before)
    new_file = load(file_path_after)
    diff = build(old_file, new_file)
    formatter = RENDERERS.get(format_name)
    return formatter(diff)
