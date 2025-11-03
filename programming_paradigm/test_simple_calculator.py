import unittest
from simple_calculator import SimpleCalculator



class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(1 , 6), 7)
        
    def test_add_negative(self):
        self.assertEqual(self.calc.add(8, -5), 3)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8, 3), 5)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 8), 24)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
         
    def test_divison_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
            
    def test_divide_negative_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(-8, 0)
            
    def test_divide_zero_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(0, 0)
if __name__ == "__main__":
    unittest.main()
            