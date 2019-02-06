import unittest

from myint import MyInt
from purely_imaginary_number import PurelyImaginaryNumber


class TestPurelyImaginaryNumber(unittest.TestCase):
    def test_purely_imaginary_number(self):
        with self.subTest('create 4i'):
            i_4 = PurelyImaginaryNumber(MyInt(4))
            expected = '4i'
            actual = str(i_4)
            self.assertEqual(expected, actual)

        with self.subTest('create -2i'):
            minus_i_2 = PurelyImaginaryNumber(MyInt(-2))
            expected = '-2i'
            actual = str(minus_i_2)
            self.assertEqual(expected, actual)

    def test_raise_zero_error(self):
        with self.assertRaises(ValueError):
            PurelyImaginaryNumber(MyInt(0))

    def test_purely_imaginary_number_with_1(self):
        with self.subTest('create i'):
            i_1 = PurelyImaginaryNumber(MyInt(1))
            expected = 'i'
            actual = str(i_1)
            self.assertEqual(expected, actual)

        with self.subTest('create -i'):
            minus_i_1 = PurelyImaginaryNumber(MyInt(-1))
            expected = '-i'
            actual = str(minus_i_1)
            self.assertEqual(expected, actual)

    def test_check_equality(self):
        with self.subTest('check being equal'):
            i_4_1 = PurelyImaginaryNumber(MyInt(4))
            i_4_2 = PurelyImaginaryNumber(MyInt(4))
            self.assertTrue(i_4_1 == i_4_2)

        with self.subTest('check not being equal'):
            i_4 = PurelyImaginaryNumber(MyInt(4))
            i_2 = PurelyImaginaryNumber(MyInt(2))
            self.assertFalse(i_4 == i_2)

    def test_conjugate(self):
        with self.subTest('check 4'):
            i_4 = PurelyImaginaryNumber(MyInt(4))
            minus_i_4 = PurelyImaginaryNumber(MyInt(-4))
            self.assertTrue(i_4.is_conjugate_to(minus_i_4))

        with self.subTest('check 1'):
            i_1 = PurelyImaginaryNumber(MyInt(1))
            minus_i_1 = PurelyImaginaryNumber(MyInt(-1))
            self.assertTrue(i_1.is_conjugate_to(minus_i_1))


if __name__ == '__main__':
    unittest.main()
