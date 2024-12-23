
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
        assert checkout_solution.checkout("ABCDABAAEEE") == 365

    def test_checkout_special_offer_E2 (self ):
        assert checkout_solution.checkout("ABCDAABABAEE") == 360

    def test_checkout_A5(self ):
        assert checkout_solution.checkout("") == 0
    
    def test_checkout_A6 (self ):
        assert checkout_solution.checkout("AAAAAA") == 250

    def test_checkout_A7(self ):
        assert checkout_solution.checkout("AAAAAAA") == 300

    def test_checkout_A8 (self ):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_checkout_A9 (self ):
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    def test_checkout_A5(self ):
        assert checkout_solution.checkout("FFF") == 20
    