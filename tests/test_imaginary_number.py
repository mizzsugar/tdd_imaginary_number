import unittest

from imaginary_number import ImaginaryNumber
from purely_imaginary_number import PurelyImaginaryNumber


class TestImaginaryNumber(unittest.TestCase):
    def test_create_imaginary_number(self):
        with self.subTest('2 + 4i'):
            i4 = PurelyImaginaryNumber(4)
            i2_4 = ImaginaryNumber(2, i4)
            expected = '2 + 4i'
            actual = str(i2_4)
            self.assertEqual(expected, actual)

        with self.subTest('2 - 4i'):
            minus_i4 = PurelyImaginaryNumber(-4)
            i2_minus4 = ImaginaryNumber(2, minus_i4)
            expected = '2 - 4i'
            actual = str(i2_minus4)
            self.assertEqual(expected, actual)

        with self.subTest('real part is 0'):
            i4 = PurelyImaginaryNumber(4)
            with self.assertRaises(ValueError):
                ImaginaryNumber(0, i4)


if __name__ == '__main__':
    unittest.main()
