'''
    The main file for the solver.
    Example usage: solve([1,2,3,4])
    Returns the first solution found. (no other solutions are searched for..)
'''

from itertools import permutations, product
from typing import Generator

from calculator import calculate

operators = ['+', '-', '*', '/']
operatorlist: list = list(product(operators, repeat=3))

bracket_positions = [
    (0, 0),
    (0, 2),
    (2, 4),
    (4, 6),
    (0, 4),
    (2, 6)
]


def assemble_calculation(numbers: list, operations: list, brackets: tuple) -> list:
    '''Assembles the calculation from the list of numbers and operators.'''
    calculation = [numbers[0]]
    for i, operation in enumerate(operations):
        calculation.append(operation)
        calculation.append(numbers[i+1])
    if brackets != (0, 0):
        calculation.insert(brackets[1]+1, ')')
        calculation.insert(brackets[0], '(')
    return calculation


def generate_calculations(numbers: list) -> Generator:
    '''Generates all possible calculations'''
    for nums in permutations(numbers):
        for ops in operatorlist:
            for brackets in bracket_positions:
                yield assemble_calculation(nums, ops, brackets)


def solve(numbers: list, return_all_solutions: bool = False) -> list:
    '''Solves the puzzle.. :)'''
    solutions = list()
    for calculation in generate_calculations(numbers):
        try:
            if 10 == calculate(calculation.copy()):
                if return_all_solutions:
                    solutions.append(calculation)
                else:
                    return [calculation]
        except ZeroDivisionError:
            pass
    return solutions
