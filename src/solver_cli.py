import sys
from typing import Tuple
from solver import NoSolutionException, solve
import argparse


def parse_arguments() -> Tuple[int, int, int, int]:
    parser = argparse.ArgumentParser(description='Solver for 4=10 game')
    parser.add_argument(
        'numbers',
        nargs=4,
        metavar='number',
        type=int,
        help='Add 4 numbers to solve the problem.'
    )

    args = parser.parse_args()
    return args.numbers


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
