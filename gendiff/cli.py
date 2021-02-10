import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=['plain', 'json', 'stylish'],
        default='stylish',
        help='set format of output (default: stylish)',
    )
    return parser.parse_args()
