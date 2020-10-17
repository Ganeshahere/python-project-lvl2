# -*- coding: utf-8 -*-


"""Comparator of files."""

import json


def diff(file1, file2):
    """Should return difference between two files."""
    diff = {}

    for key in file1:
        if key in file2:
            if file1[key] == file2[key]:
                diff['  {key}'.format(key=key)] = file1[key]
            else:
                diff['- {key}'.format(key=key)] = file1[key]
                diff['+ {key}'.format(key=key)] = file2[key]
        else:
            diff['- {key}'.format(key=key)] = file1[key]

    for key in file2:
        if key not in file1:
            diff['+ {key}'.format(key=key)] = file2[key]

    print(''.json(json.dumps(diff, indent=2).split('"')))
    return diff
