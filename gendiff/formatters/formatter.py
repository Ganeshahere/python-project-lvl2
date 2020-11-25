# -*- coding:utf-8 -*-

"""Render facade module."""
from gendiff.formatters import build, text

formats = {
    'text': lambda ast: text.format_ast(ast),
    'plain': lambda ast: build.format_ast(ast),
}


def format_ast(diff_ast, result_format):
    """Format diff_ast in result format."""
    if result_format not in formats:
        raise AttributeError(
            'Result format {format} not supported'.format(format=result_format),
        )
    format_func = formats[result_format]
    return format_func(diff_ast)
