import unittest

from complex_number.imaginary_number import ImaginaryNumber
from complex_number.myint import MyInt
from complex_number.purely_imaginary_number import PurelyImaginaryNumber


class TestImaginaryNumber(unittest.TestCase):
    def test_create_imaginary_number(self):
        with self.subTest('2 + 4i'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            i2_4 = ImaginaryNumber(2, i4)
            expected = '2 + 4i'
            actual = str(i2_4)
            self.assertEqual(expected, actual)

        with self.subTest('2 - 4i'):
            minus_i4 = PurelyImaginaryNumber(MyInt(-4))
            i2_minus4 = ImaginaryNumber(2, minus_i4)
            expected = '2 - 4i'
            actual = str(i2_minus4)
            self.assertEqual(expected, actual)

        with self.subTest('real part is 0'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            with self.assertRaises(ValueError):
                ImaginaryNumber(0, i4)

    def test_check_equality(self):
        with self.subTest('check being equal'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            i2_4_1 = ImaginaryNumber(2, i4)
            i2_4_2 = ImaginaryNumber(2, i4)
            self.assertTrue(i2_4_1 == i2_4_2)

        with self.subTest('check not being equal'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            i2_4 = ImaginaryNumber(2, i4)
            i2 = PurelyImaginaryNumber(MyInt(2))
            i2_2 = ImaginaryNumber(2, i2)
            self.assertFalse(i2_4 == i2_2)

    def test_is_conjugate(self):
        with self.subTest('2+4i and 2-4i'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            minus_i4 = PurelyImaginaryNumber(MyInt(-4))
            i2_4 = ImaginaryNumber(2, i4)
            minus_i2_4 = ImaginaryNumber(2, minus_i4)
            self.assertTrue(i2_4.is_conjugate_to(minus_i2_4))

    def test_not_conjugate(self):
        with self.subTest('2+4i and 3-4i'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            minus_i4 = PurelyImaginaryNumber(MyInt(-4))
            i2_4 = ImaginaryNumber(2, i4)
            minus_i2_4 = ImaginaryNumber(3, minus_i4)
            self.assertFalse(i2_4.is_conjugate_to(minus_i2_4))

        with self.subTest('2+4i and -2-4i'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            minus_i4 = PurelyImaginaryNumber(MyInt(-4))
            i2_4 = ImaginaryNumber(2, i4)
            minus_i2_4 = ImaginaryNumber(-2, minus_i4)
            self.assertFalse(i2_4.is_conjugate_to(minus_i2_4))


if __name__ == '__main__':
    unittest.main()
