# -*- coding:utf-8 -*-

"""Module with renderers from diff_ast."""
from gendiff.constants import ADDED, CHANGED, NESTED, REMOVED, UNCHANGED


def render(diff_ast):
    """Test message diff from diff_ast function result."""
    return '{{\n{lines}\n}}'.format(
        lines=_message_lines(diff_ast),
    )


def _message_lines(diff_ast, depth=0):
    lines = []
    for key in sorted(diff_ast.keys()):
        node = diff_ast[key]
        if node['type'] == NESTED:
            children = _message_lines(node['children'], depth=depth + 1)
            line = f'    {_get_prefix(depth)}{key}: {{\n{children}\n    {_get_prefix(depth)}}}'
        if node['type'] == CHANGED:
            line = '{added}\n{removed}'.format(
                added=_get_build_message(
                    symbol='+',
                    key=key,
                    value=node['value'],
                    depth=depth,
                ),
                removed=_get_build_message(
                    symbol='-',
                    key=key,
                    value=node['oldValue'],
                    depth=depth,
                ),
            )
        if node['type'] == UNCHANGED:
            line = _get_build_message(
                symbol=' ',
                key=key,
                value=node['value'],
                depth=depth,
            )
        if node['type'] == ADDED:
            line = _get_build_message(
                symbol='+',
                key=key,
                value=node['value'],
                depth=depth,
            )
        if node['type'] == REMOVED:
            line = _get_build_message(
                symbol='-',
                key=key,
                value=node['value'],
                depth=depth,
            )
        lines.append(line)
    return '\n'.join(lines)


def _get_build_message(symbol, key, value, depth):
    return f'{_get_prefix(depth)}  {symbol} {key}: {_get_value(value, depth + 1)}'


def _get_value(value, depth):
    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        return _value_dict(value, depth)
    return value


def _value_dict(sub_dict, depth):
    res = []
    for key, value in sub_dict.items():
        res.append(f'{{\n    {_get_prefix(depth)}{key}: {value}\n{_get_prefix(depth)}}}')
    return '\n'.join(res)


def _get_prefix(depth):
    return '    ' * depth
