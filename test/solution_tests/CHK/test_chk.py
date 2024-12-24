
from solutions.CHK import checkout_solution
import unittest

class TestSum(unittest.TestCase):
    # def test_checkout_type(self):
    #     assert checkout_solution.checkout(True) == -1

    # def test_checkout_bad_input(self):
    #     assert checkout_solution.checkout("AAB1") == -1

    # def test_checkout_sum (self):
    #     assert checkout_solution.checkout("A") == 50

    # def test_checkout_sum_2 (self ):
    #     assert checkout_solution.checkout("ABCDA") == 165

    # def test_checkout_special_offer_B (self ):
    #     assert checkout_solution.checkout("ABCDAB") == 180
    
    # def test_checkout_special_offer_A (self ):
    #     assert checkout_solution.checkout("ABCDABAA") == 260
    
    # def test_checkout_special_offer_E (self ):
    #     assert checkout_solution.checkout("ABCDABAAEEEFFF") == 385

    # def test_checkout_special_offer_E2 (self ):
    #     assert checkout_solution.checkout("EE") == 80

    # def test_checkout_A5(self ):
    #     assert checkout_solution.checkout("") == 0
    
    # def test_checkout_A6 (self ):
    #     assert checkout_solution.checkout("AAAAAA") == 250

    # def test_checkout_A7(self ):
    #     assert checkout_solution.checkout("AAAAAAA") == 300

    # def test_checkout_A8 (self ):
    #     assert checkout_solution.checkout("AAAAAAAA") == 330

    # def test_checkout_A9 (self ):
    #     assert checkout_solution.checkout("AAAAAAAAA") == 380

    # def test_checkout_F(self ):
    #     assert checkout_solution.checkout("FFFFFF") == 40

    # def test_checkout_H5(self):
    #     assert checkout_solution.checkout("HHHHH") == 45

    # def test_checkout_H6(self):
    #     assert checkout_solution.checkout("HHHHHH") == 55

    # def test_bsogsof(self):
    #     assert checkout_solution.checkout("BBB") == 75

    # def test_one_of_each_F(self):
    #     assert checkout_solution.checkout("F") == 10

    # def test_one_of_each_H(self):
    #     assert checkout_solution.checkout("H") == 10

    # def test_one_of_eachK(self):
    #     assert checkout_solution.checkout("KK") == 150

    # def test_one_of_eachM(self):
    #     assert checkout_solution.checkout("M") == 15

    # def test_one_of_eachP(self):
    #     assert checkout_solution.checkout("P") == 50
    
    # def test_one_of_eachQ(self):
    #     assert checkout_solution.checkout("Q") == 30

    # def test_one_of_eachU(self):
    #     assert checkout_solution.checkout("U") == 40

    # def test_one_of_eachV(self):
    #     assert checkout_solution.checkout("V") == 50

    def test_discount_group(self):
        assert checkout_solution.checkout("STVZ") == 25

    def test_discount_groupZ(self):
        assert checkout_solution.checkout("ZZZZZ") == 45

    def test_discount_group(self):
        assert checkout_solution.checkout("STXY") == 62

    def test_discount_group(self):
        assert checkout_solution.checkout("STZY") == 65
