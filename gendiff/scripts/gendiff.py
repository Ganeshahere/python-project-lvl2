from gendiff.parsers import get_parser
from gendiff.comparator import generate_diff


def main():
    """Run cli."""
    args = get_parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()