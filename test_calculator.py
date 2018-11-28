"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator(object):

    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(a, b):
        assert 100 == calculator.multiply(10, 10)
