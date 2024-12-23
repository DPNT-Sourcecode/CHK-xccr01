
from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):
    def test_checkout_type(self):
        assert checkout_solution.checkout(True) == -1

    def test_checkout_bad_input(self):
        assert checkout_solution.checkout("AABZ") == -1

    def test_checkout_sum (self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_sum_2 (self ):
        assert checkout_solution.checkout("ABCDA") == 165

    def test_checkout_special_offer_B (self ):
        assert checkout_solution.checkout("ABCDAB") == 180
    
    def test_checkout_special_offer_A (self ):
        assert checkout_solution.checkout("ABCDABAA") == 260
    
    def test_checkout_special_offer_E (self ):
        assert checkout_solution.checkout("ABCDABAAEEE") == 245


