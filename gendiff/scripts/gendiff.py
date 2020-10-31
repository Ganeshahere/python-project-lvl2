#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Gendiff script."""

import argparse

from gendiff import comparator


def main():
    """Print diff between two files also argument parser."""
    parser = argparse.ArgumentParser(
            prog='gendiff',
            usage='%(prog)s [-h] [-f FORMAT] first_file second_file',
            description='Generate diff')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument(
            '-f',
            '--format',
            help='set format of output',
            )
    args = parser.parse_args()
    diff = comparator.generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
