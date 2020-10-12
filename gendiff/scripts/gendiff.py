#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Gendiff script."""

import argparse


def main():
    """Print diff between two files."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    args = parser.parse_args()
    print(args.format)


if __name__ == '__main__':
    main()
