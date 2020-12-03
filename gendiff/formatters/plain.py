# -*- coding: utf-8 -*-

"""Building formatter from diff ast."""
from gendiff.constants import ADDED, CHANGED, PARENT, REMOVED


def format_ast(diff):
    """Build message diff from diff_ast function result."""
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
                "Property '{key}' was changed. From '{old}' to '{new}'".format(
                    key=_get_path(parents, key),
                    old=_get_value(node['oldValue']),
                    new=_get_value(node['value']),
                ),
            )
        if node['type'] == ADDED:
            lines.append(
                "Property '{key_path}' was added with value: '{value}'".format(
                    key_path=_get_path(parents, key),
                    value=_get_value(node['value']),
                ),
            )
        if node['type'] == REMOVED:
            lines.append("Property '{key_path}' was removed".format(
                key_path=_get_path(parents, key),
            ))
    return '\n'.join(lines)


def _get_value(value):
    if isinstance(value, dict):
        return 'complex value'
    return value


def _get_path(parents, key):
    return '.'.join(parents + [key])
