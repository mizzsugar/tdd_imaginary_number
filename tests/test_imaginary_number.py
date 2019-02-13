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

        with self.subTest('0 + 4i'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            i0_4 = ImaginaryNumber(0, i4)
            expected = '4i'
            actual = str(i0_4)
            self.assertEqual(expected, actual)

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


if __name__ == '__main__':
    unittest.main()
