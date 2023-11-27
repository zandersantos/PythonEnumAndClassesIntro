"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(TestCase):
    
    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            Mortgage(0,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        
        with self.assertRaises(ValueError):
            Mortgage(-1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
            
    def test_invalid_rate_value(self):
        with self.assertRaises(ValueError):
            Mortgage(1,0,MortgageFrequency.BI_WEEKLY,5)
            
    def test_invalid_freq_value(self):
        with self.assertRaises(ValueError):
            Mortgage(1,MortgageRate.FIXED_1,0,5)
            
    def test_invalid_amort_value(self):
        with self.assertRaises(ValueError):
            Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,40)
    
    def test_loanamount_negative(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(ValueError):
            expected.LoanAmount = -1
    
    def test_loanamount_zero(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(ValueError):
            expected.LoanAmount = 0
    
    def test_loanamount_positive(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        expected.LoanAmount = 1
        self.assertEqual(expected.LoanAmount,1)

if __name__ == '__main__':
    TestCase.main()





