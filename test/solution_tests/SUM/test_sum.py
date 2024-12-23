
from solutions.SUM import sum_solution
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_dif_sum(self):
        assert sum_solution.compute(5, 2) == 7\
    
    def test_neg_sum(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(-5, -2)

    def test_y_neg_sum(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(5, -2)

    def test_large_sum(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(1001, 500)

    def test_y_large_sum(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(1, 500)
    
    def test_type_sum(self):
        with self.assertRaises(TypeError):
            sum_solution.compute('a', True)



