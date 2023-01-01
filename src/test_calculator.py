import unittest
from calculator import calculate


class CalculatorTest(unittest.TestCase):
    '''Calculator'''

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_calculator(self):
        '''Basic calculations'''
        cases2 = [
            '1 + 2 = 3',
            '4 + 6 = 10',
            '11 + 2 = 13',
            '17 + 5 = 22',
            '22 + 33 = 55',
            '3 + 4 + 1 = 8',

            '1 - 2 = -1',
            '4 - 6 = -2',
            '11 - 2 = 9',
            '17 - 5 = 12',
            '22 - 33 = -11',
            '3 - 4 - 1 = -2',

            '1 * 2 = 2',
            '4 * 6 = 24',
            '11 * 2 = 22',

            '9 / 3 = 3',
            '100 / 25 = 4',
            '50 / 5 = 10',
            '10 / 4 = 2.5',

            '10 / 4 + 3 = 5.5',
            '10 + 4 * 3 = 22',

            '1 + 3 = 4',
            '8 - 4 + 1 = 5',
            '2 + 5 + 7 - 2 * 3 = 8',
            '2 + 5 + 7 - 2 / 2 * 3 = 11',

            '( 1 + 1 ) + 1 = 3',
            '1 + ( 2 + 1 ) = 4',
            '1 + ( 2 + 1 ) * 3 = 10',
            '1 + ( 2 / 1 ) * 3 + 6 / 3 = 9',
            '12 / ( 2 + 1 ) = 4',
            '40 - 2 * ( 1 + 4 / 2 ) * 3 - 6 / 2 = 19'
        ]
        for case in cases2:
            elements, result = [int(x) if x.strip().isnumeric() else x for x in case.split(" = ")]
            elements, result = case.split(" = ")
            result = float(result)
            ops = [int(x) if x.isnumeric() else x for x in elements.split(" ")]
            print(f'{elements} == {result} ... ', end='')
            self.assertEqual(calculate(ops), result, 'Incorrect answer!')
            print('ok')
