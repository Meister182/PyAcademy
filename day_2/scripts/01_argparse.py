import os
import argparse

# call: python3 01_argparse.py -h
# experiment passing it different arguments

def argument_parser():
    """Method to handle script arguments"""
    parser = argparse.ArgumentParser(
        description="A simple script to test argparse. Analagous to the snipets in Packagers.ipynb."
    )

    # Positional arguments
    parser.add_argument("input_1", type=int)
    parser.add_argument("input_2", type=str)

    # flag arguments
    # string
    parser.add_argument(
        "-s", "--string",
        type=str,
        help="A string delivered by flag.",
        required=True
    )

    # list
    parser.add_argument(
        "-l", "--list",
        nargs=3,
        dest="list3",
        help="A list argument of 3 elements.",
    )

    # Boolean
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="A simple debug flag."
    )

    group = parser.add_mutually_exclusive_group()

    # Add arguments to the group
    group.add_argument('--file', action='store_true', help="Use a file path.")
    group.add_argument('--dir', action='store_false', help="Use a dir path.")

    return parser.parse_args()


if __name__ == "__main__":
    args = argument_parser()
    print(args)