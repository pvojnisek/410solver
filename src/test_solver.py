'''
    Testing solver functions.
'''
import unittest
from solver import assemble_calculation, generate_calculations, solve


class SolverTest(unittest.TestCase):
    '''SolverTest class'''
    cases = [
        ([1, 3, 4, 2], '1+3+4+2'),
    ]

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_calculus_assember(self):
        '''Assembly of calculations'''
        ops = ['+', '-', '*']
        numbers = [1, 2, 3, 4]
        result = [1, '+', 2, '-', 3, '*', 4]
        self.assertListEqual(assemble_calculation(numbers, ops, (0, 0)), result, 'Assembled calculus is not correct!')

    def test_gerating_calculations(self):
        '''Number of generated permutations'''
        self.assertEqual(len(list(generate_calculations([1, 2, 3, 4]))), 4*3*2*1 * 4*4*4 * 6, 'The length of permutations are not correct!')

    def test_basic_functions(self):
        '''Possible solutions'''
        cases = [
            ([1, 2, 3, 4], [[1, '+', 2, '+', 3, '+', 4]]),
            ([2, 5, 4, 2], [['(', 2, '+', 5, ')', '*', 2, '-', 4]]),
            ([7, 3, 3, 1], [['(', 7, '/', 3, '+', 1, ')', '*', 3]]),
        ]
        for case in cases:
            print(case)
            self.assertListEqual(solve(case[0]), case[1])

        #print(solve([3, 3, 7, 1]))
