# -*- coding:utf-8 -*-

"""Renderers from diff_ast."""
import json

from gendiff.nodetypes import PARENT


def format_ast(diff_ast):
    """Test message diff from diff_ast function result."""
    filtered_ast = _build_ast(diff_ast)
    return json.dumps(filtered_ast)


def _build_ast(ast):
    result = {}
    for key, node in ast.items():
        if node['type'] == PARENT:
            result[key] = _build_ast(node['children'])
        else:
            result[key] = node
    return result
