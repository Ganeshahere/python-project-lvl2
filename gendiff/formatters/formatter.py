# -*- coding:utf-8 -*-

"""Render facade module."""
from gendiff.formatters import build, text

formats = {
    'text': lambda ast: text.format_ast(ast),
    'build': lambda ast: build.format_ast(ast),
}


def format_ast(diff_ast, result_format):
    """Format diff_ast in result format."""
    if result_format not in formats:
        raise AttributeError(
            f'Result format {result_format} not supported',
        )
    format_func = formats[result_format]
    return format_func(diff_ast)
