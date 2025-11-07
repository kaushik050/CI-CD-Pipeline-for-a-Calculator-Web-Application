"""
Unit tests for Calculator application
Tests all arithmetic operations and edge cases
"""

import unittest
from calculator import Calculator

try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertEqual(self.calc.add(0, 5), 5)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers"""
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)
    
    def test_add_decimal_numbers(self):
        """Test addition with decimal numbers"""
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=10)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 7), 3)
        self.assertEqual(self.calc.subtract(5, 5), 0)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers"""
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
    
    def test_subtract_decimal_numbers(self):
        """Test subtraction with decimal numbers"""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2, places=10)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=10)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(5, 0), 0)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers"""
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(-10, 5), -50)
        self.assertEqual(self.calc.multiply(10, -5), -50)
    
    def test_multiply_decimal_numbers(self):
        """Test multiplication with decimal numbers"""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0, places=10)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=10)
    
    def test_divide_positive_numbers(self):
        """Test division with positive numbers"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333333333333335, places=10)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers"""
        self.assertEqual(self.calc.divide(-6, -2), 3)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(10, -5), -2)
    
    def test_divide_decimal_numbers(self):
        """Test division with decimal numbers"""
        self.assertAlmostEqual(self.calc.divide(5.5, 2.5), 2.2, places=10)
        self.assertAlmostEqual(self.calc.divide(0.3, 0.1), 3.0, places=10)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
        
        with self.assertRaises(ValueError):
            self.calc.divide(-5, 0)
    
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
    
    def test_power_negative_numbers(self):
        """Test power operation with negative numbers"""
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertEqual(self.calc.power(-3, 3), -27)
    
    def test_power_decimal_numbers(self):
        """Test power operation with decimal numbers"""
        self.assertAlmostEqual(self.calc.power(2.5, 2), 6.25, places=10)
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0, places=10)


if HAS_PYTEST:
    class TestCalculatorPytest:
        """Additional pytest-style tests for Calculator class"""
        
        @pytest.fixture
        def calculator(self):
            """Fixture to create calculator instance"""
            return Calculator()
        
        def test_add_edge_cases(self, calculator):
            """Test addition edge cases"""
            assert calculator.add(0, 0) == 0
            assert calculator.add(1e10, 1e10) == 2e10
        
        def test_multiply_edge_cases(self, calculator):
            """Test multiplication edge cases"""
            assert calculator.multiply(1, 1) == 1
            assert calculator.multiply(0, 100) == 0
        
        def test_divide_edge_cases(self, calculator):
            """Test division edge cases"""
            assert calculator.divide(0, 5) == 0
            assert calculator.divide(1, 1) == 1
        
        def test_power_edge_cases(self, calculator):
            """Test power edge cases"""
            assert calculator.power(1, 100) == 1
            assert calculator.power(0, 5) == 0


if __name__ == '__main__':
    # Run unittest tests
    unittest.main(verbosity=2)
