import unittest

from complex_number.imaginary_number import ImaginaryNumber
from complex_number.myint import MyInt
from complex_number.purely_imaginary_number import PurelyImaginaryNumber


class TestImaginaryNumber(unittest.TestCase):
    def test_create_imaginary_number(self):
        with self.subTest('2 + 4i'):
            i2_4 = ImaginaryNumber(2, MyInt(4))
            expected = '2 + 4i'
            actual = str(i2_4)
            self.assertEqual(expected, actual)

        with self.subTest('2 - 4i'):
            i2_minus4 = ImaginaryNumber(2, MyInt(-4))
            expected = '2 - 4i'
            actual = str(i2_minus4)
            self.assertEqual(expected, actual)

        with self.subTest('0 + 4i'):
            i0_4 = ImaginaryNumber(0, MyInt(4))
            expected = '4i'
            actual = str(i0_4)
            self.assertEqual(expected, actual)

    def test_check_equality(self):
        with self.subTest('check being equal'):
            i2_4_1 = ImaginaryNumber(2, MyInt(4))
            i2_4_2 = ImaginaryNumber(2, MyInt(4))
            self.assertTrue(i2_4_1 == i2_4_2)

        with self.subTest('check not being equal'):
            i2_4 = ImaginaryNumber(2, MyInt(4))
            i2_2 = ImaginaryNumber(2, MyInt(2))
            self.assertFalse(i2_4 == i2_2)

    def test_real_is_0(self):
        i4 = PurelyImaginaryNumber(MyInt(4))
        i0_4 = ImaginaryNumber(0, MyInt(4))
        self.assertTrue(i0_4 == i4)

    def test_conjugate_pure_0(self):
        with self.subTest('start with PurelyImaginaryNum'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            minus_i0_4 = ImaginaryNumber(0, MyInt(-4))
            self.assertTrue(minus_i0_4.is_conjugate_to(i4))

        with self.subTest('start with ImaginaryNum'):
            i4 = PurelyImaginaryNumber(MyInt(4))
            minus_i0_4 = ImaginaryNumber(0, MyInt(-4))
            self.assertTrue(i4.is_conjugate_to(minus_i0_4))


if __name__ == '__main__':
    unittest.main()
