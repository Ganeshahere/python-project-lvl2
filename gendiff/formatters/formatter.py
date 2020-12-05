# -*- coding:utf-8 -*-

"""Render facade module."""
from gendiff.formatters import plain, stylish, json

formats = {
    'json': lambda ast: json.render(ast),
    'stylish': lambda ast: stylish.render(ast),
    'plain': lambda ast: plain.render(ast),
}


def format_ast(diff_ast, result_format):
    """Format diff_ast in result format."""
    if result_format not in formats:
        raise AttributeError(
            f'Result format {result_format} not supported',
        )
    format_func = formats[result_format]
    return format_func(diff_ast)
