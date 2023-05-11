import unittest
from math import pi

import circles


class TestCircleArea(unittest.TestCase):
    def test_values(self):
        self.assertRaises(ValueError, circles.circle_area, -2)

    def test_area(self):
        self.assertAlmostEqual(circles.circle_area(1), pi)
        self.assertAlmostEqual(circles.circle_area(0), 0)
        self.assertAlmostEqual(circles.circle_area(2.1), pi * 2.1 ** 2)
