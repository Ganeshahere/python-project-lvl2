# -*- coding:utf-8 -*-

"""Renderers from diff dict."""

from gendiff.nodetypes import ADDED, CHANGED, PARENT, REMOVED, UNCHANGED


def build(diff):
    """Build message difference from diff_dict function result."""
    return '{{\'n{lines}\n}}'.format(
        lines=_build_message_lines(diff),
    )


def _build_message_lines(diff, depth=0):
    lines = []
    for key in sorted(diff.keys()):
        node = diff[key]
        if node['type'] == PARENT:
            children = _build_message_lines(node['children'], depth=depth + 1)
            line = '    {prefix}{key}: {{\n{children}\n    {prefix}}}'.format(
                children=children,
                key=key,
                prefix=_get_prefix(depth),
            )
            if node['type'] == CHANGED:
                line = '{added}\n{removed}'.format(
                    added=_get_build_message(
                        key=key,
                        symbol='+',
                        value=node['value'],
                        depth=depth,
                    ),
                    removed=_get_build_message(
                        symbol='-',
                        key=key,
                        value=node['oldValue'],
                        depth=depth
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
    return '{prefix}  {symbol} {key}: {value}'.format(
        symbol=symbol,
        key=key,
        value=_get_value(value, depth + 1),
        prefix=_get_prefix(depth),
    )


def _get_value(value, depth):
    if isinstance(value, dict):
        return _value_dict(value, depth)
    return value


def _value_dict(sub_dict, depth):
    res = []
    for key, value in sub_dict.items():
        res.append('{{\n    {prefix}{key}: {value}\n{prefix}}}'.format(
            key=key,
            value=value,
            prefix=_get_prefix(depth),
        ))
    return '\n'.join(res)


def _get_prefix(depth):
    return '    ' * depth
