"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        """unit test for addition"""
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        """unit test for substration    """
        assert 2 == calculator.subtract(4, 2)