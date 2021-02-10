from gendiff.formatters import json, plain, stylish


RENDERERS = {
    'json': json.render,
    'plain': plain.render,
    'stylish': stylish.render,
}
