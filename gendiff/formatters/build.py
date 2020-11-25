# -*- coding: utf-8 -*-

"""Building formatter from diff ast."""
from gendiff.nodetypes import ADDED, CHANGED, PARENT, REMOVED


def format_ast(diff):
    """Plain message diff from diff_ast function result."""
    return _message_lines(diff)


def _message_lines(diff, parents=None):
    if not parents:
        parents = []

    lines = []
    for key in sorted(diff.keys()):
        node = diff[key]

        if node['type'] == PARENT:
            lines.append(
                _message_lines(node['children'], parents=parents + [key]),
            )
        if node['type'] == CHANGED:
            lines.append(
                f"Property '{_get_path(parents, key)}' was changed. From '{_get_value(node['oldValue'])}'\
                 to '{_get_value(node['value'])}'",
            )
        if node['type'] == ADDED:
            lines.append(
                f"Property '{_get_path(parents, key)}' was added with value: '{_get_value(node['value'])}'",
            )
        if node['type'] == REMOVED:
            lines.append(f"Property '{_get_path(parents, key)}' was removed")
    return '\n'.join(lines)


def _get_value(value):
    if isinstance(value, dict):
        return 'complex value'
    return value


def _get_path(parents, key):
    return '.'.join(parents + [key])
