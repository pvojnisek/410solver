from curses import meta
import sys
from typing import Tuple
from solver import NoSolutionException, solve
import argparse


def parse_arguments() -> Tuple[int, int, int, int]:
    parser = argparse.ArgumentParser(
        prog='Solver for 4=10 game',
        description='You can download the game from play store for Android.',
        epilog='Please use this utility only when you stuck. Using it too much can harm the gaming experience.'
    )
    parser.add_argument(
        '--numbers',
        nargs=4,
        metavar='number',
        type=int,
        help='Add 4 numbers to solve the problem.'
    )

    parser.add_argument(
        '--shortnumbers',
        nargs=1,
        # metavar('shortnumber'),
        type=int,
        help='define numbers without spaces. Example: abcd'
    )

    args = parser.parse_args()
    print('===>', args)
    if args.shortnumbers:
        return [int(x) for x in str(args.shortnumbers[0])]
    elif args.numbers:
        return args.numbers
    else:
        raise NotImplementedError('Argument is not implemented: '+str(args))

    return args.numbers if args.numbers else [int(x) for x in str(args.shortnumbers[0])]


def main():
    numbers = parse_arguments()
    print('4=10 solver!')
    print('The problem is: ', numbers)
    try:
        solution = solve(numbers)
    except NoSolutionException:
        print('Unfortunatelly there is no solution for this problem!')
        sys.exit()
    print('And the solution is: ', ' '.join([str(x) for x in solution]))


if __name__ == "__main__":
    main()
