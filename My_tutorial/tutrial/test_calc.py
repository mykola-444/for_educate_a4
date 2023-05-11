import unittest

import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
#        result = calc.add(10, 5)
        self.assertAlmostEqual(calc.add(10, 5), 14)


if __name__ == '__main__':
    unittest.main()
