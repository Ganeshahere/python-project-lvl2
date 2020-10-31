# -*- coding:utf-8 -*-

"""Formatters functions from diff dictionaries."""


def build_message(diff):
    """Build message diff from diff_dict function result."""
    message_format = ' {symbol} {key}: {value}'

    unchanged_messages = [
        message_format.format(symbol=' ', key=key, value=value)
        for key, value in diff['unchanged'].items()
    ]
    changed_messages = sum(
        [
            [
                message_format.format(symbol='+', key=key, value=value['new']),
                message_format.format(symbol='-', key=key, value=value['old']),
            ]
            for key, value in diff['changed'].items()
        ],
        [],
    )
    removed_messages = [
        message_format.format(symbol='-', key=key, value=value)
        for key, value in diff['removed'].items()
    ]
    added_messages = [
        message_format.format(symbol='+', key=key, value=value)
        for key, value in diff['added'].items()
    ]

    messsage = [
        '{',
        *unchanged_messages,
        *changed_messages,
        *removed_messages,
        *added_messages,
        '}'
    ]
    return '\n'.join(messsage)
