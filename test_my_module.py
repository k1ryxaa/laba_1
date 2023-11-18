import unittest
from math import cos, pi, sqrt

class CosFunctionTestCase(unittest.TestCase):
    def test_cos_zero(self):
        self.assertAlmostEqual(cos(0), 1.0)

    def test_cos_pi_half(self):
        self.assertAlmostEqual(cos(pi / 2), 0.0)

    def test_cos_pi(self):
        self.assertAlmostEqual(cos(pi), -1.0)

    def test_cos_three_pi_half(self):
        self.assertAlmostEqual(cos(3 * pi / 2), 0.0)

    def test_cos_two_pi(self):
        self.assertAlmostEqual(cos(2 * pi), 1.0)

    # Дополнительный тест на произвольное значение
    def test_cos_arbitrary(self):
        # Значение cos(π/4) должно быть равно sqrt(2)/2
        self.assertAlmostEqual(cos(pi / 4), sqrt(2)/2)