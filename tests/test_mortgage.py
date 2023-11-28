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
        self.assertEqual(expected.LoanAmount, 1)
        
    def test_freq_true(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        expected.Frequency = MortgageFrequency.BI_WEEKLY
        self.assertEqual(expected.Frequency, MortgageFrequency.BI_WEEKLY)
    
    def test_freq_false(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(ValueError):
            expected.Frequency = ""
            
    def test_amort_true(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        expected.Amortization = 5
        self.assertEqual(expected.Amortization, 5)
    
    def test_amort_false(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(Exception):
            expected.Amortization = 1
    
    def test_init(self):
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)

        self.assertEqual(expected.LoanAmount,1)
        self.assertEqual(expected.Rate,MortgageRate.FIXED_1)
        self.assertEqual(expected.Frequency,MortgageFrequency.BI_WEEKLY)
        self.assertEqual(expected.Amortization,5)
        
    def test_calculate_payment_biweekly(self):
        #payment_result = (2 * (0.0579/26 * (1 + 0.0579/26)**(5*26))/((1+0.0579/26)**(5*26) - 1))
        payment_result = 0.02
        expected = Mortgage(2,MortgageRate.FIXED_3,MortgageFrequency.BI_WEEKLY,5)
        actual_payment = expected.calculate_payment()
        self.assertAlmostEqual(actual_payment,payment_result,places=2)
        
    def test_calculate_payment_monthly(self):
        payment_result = 4046.23
        expected = Mortgage(682912.43,MortgageRate.FIXED_1,MortgageFrequency.MONTHLY,30)
        actual_payment = expected.calculate_payment()
        self.assertAlmostEqual(actual_payment,payment_result,places=2)
        
    def test_calculate_payment_weekly(self):
        #payment_result = (10000 * ((0.05/52) * (1 + (0.05/52))**(20*52))/((1 + (0.05/52))**(20*52) - 1))
        payment_result = 15.22
        expected = Mortgage(10000,MortgageRate.FIXED_5,MortgageFrequency.WEEKLY,20)
        actual_payment = expected.calculate_payment()
        self.assertAlmostEqual(actual_payment,payment_result,places=2)

        
#(principal_loan * (interest_rate * (1 + interest_rate)**number_of_payments)/((1+interest_rate)**number_of_payments - 1))
#(2 * (0.0579 * (1 + 0.0579)**5)/((1+0.0579)**5 - 1))
        



if __name__ == '__main__':
    TestCase.main()





