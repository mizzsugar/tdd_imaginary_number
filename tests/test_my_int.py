import unittest

from complex_number.myint import MyInt


class TestMyInt(unittest.TestCase):
    def test_invalid_0(self):
        with self.assertRaises(ValueError):
            MyInt(0)


if __name__ == '__main__':
    unittest.main()
