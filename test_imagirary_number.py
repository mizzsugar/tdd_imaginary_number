import unittest
from dataclasses import dataclass


@dataclass
class PurelyImaginaryNumber:
    num: int

    def __init__(self, num) -> None:
        if num == 0:
            raise ValueError
        self.num = num

    def __str__(self) -> str:
        if self.num == 1:
            return 'i'
        elif self.num == -1:
            return '-i'
        return f'{self.num}i'


class TestImaginaryNumber(unittest.TestCase):
    def test_purely_imaginary_number(self):
        with self.subTest('create 4i'):
            i_4 = PurelyImaginaryNumber(4)
            expected = '4i'
            actual = str(i_4)
            self.assertEqual(expected, actual)

        with self.subTest('create -2i'):
            minus_i_2 = PurelyImaginaryNumber(2)
            expected = '-2i'
            actual = str(minus_i_2)
            self.assertEqual(expected, actual)

    def test_raise_zero_error(self):
        with self.assertRaises(ValueError):
            PurelyImaginaryNumber(0)

    def test_purely_imaginary_number_with_1(self):
        with self.subTest('create i'):
            i_1 = PurelyImaginaryNumber(1)
            expected = 'i'
            actual = str(i_1)
            self.assertEqual(expected, actual)

        with self.subTest('create -i'):
            minus_i_1 = PurelyImaginaryNumber(-1)
            expected = '-i'
            actual = str(minus_i_1)
            self.assertEqual(expected, actual)

    def test_check_equality(self):
        with self.subTest('check being equal'):
            i_4_1 = PurelyImaginaryNumber(4)
            i_4_2 = PurelyImaginaryNumber(4)
            self.assertTrue(i_4_1 == i_4_2)

        with self.subTest('check not being equal'):
            i_4 = PurelyImaginaryNumber(4)
            i_2 = PurelyImaginaryNumber(2)
            self.assertFalse(i_4 == i_2)


if __name__ == '__main__':
    unittest.main()
