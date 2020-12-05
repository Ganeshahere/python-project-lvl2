# -*- coding:utf-8 -*-

"""Cli module."""
import argparse

from comparator import generate_diff
from gendiff.formatters import json, stylish, plain

_FORMATS = {
    'json': json.render,
    'plain': plain.render,
    'stylish': stylish.render,
}

parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument(
    '-f',
    '--format',
    dest='FORMAT',
    choices=_FORMATS,
    default='stylish',
    help='set up output format',
)

parser.add_argument('first_file', metavar='first_file')
parser.add_argument('second_file', metavar='second_file')


def main():
    """Run cli."""
    args = parser.parse_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        format_func=_FORMATS[args.FORMAT],
    )
    print(diff)


if __name__ == '__main__':
    main()
