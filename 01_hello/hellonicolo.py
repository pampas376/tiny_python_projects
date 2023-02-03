#!/usr/bin/env python3
"""
Author : nicolo <nicolo@localhost>
Date   : 2023-02-03
Purpose: Say Hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='hello project',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', 
                        '--name', 
                        help='name to greet',
                        metavar='name',
                        type=str,
                        default='World')
        
    return parser.parse_args()


# --------------------------------------------------
def main():
    """say hello"""

    args = get_args()
    person = args.name
    print(f'Hello, {person}!')


# --------------------------------------------------
if __name__ == '__main__':

    main()
