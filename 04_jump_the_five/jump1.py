#!/usr/bin/env python3
"""
Author : nicolo <nicolo@localhost>
Date   : 2023-02-21
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get test command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    print(args.text.translate(str.maketrans(jumper)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
