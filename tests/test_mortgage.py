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
        #A test case to ensure that the __init__ raises a ValueError when an invalid amount input value is used.
        
        #Raises with a 0
        with self.assertRaises(ValueError):
            Mortgage(0,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        
        #Raises with a negative
        with self.assertRaises(ValueError):
            Mortgage(-1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
            
    def test_invalid_rate_value(self):
        #A test case to ensure that the __init__ raises a ValueError when an invalid rate input value is used.
        with self.assertRaises(ValueError):
            Mortgage(1,0,MortgageFrequency.BI_WEEKLY,5)
            
    def test_invalid_freq_value(self):
        #A test case to ensure that the __init__ raises a ValueError when an invalid frequency input value is used.
        with self.assertRaises(ValueError):
            Mortgage(1,MortgageRate.FIXED_1,0,5)
            
    def test_invalid_amort_value(self):
        #A test case to ensure that the __init__ raises a ValueError when an invalid amortization input value is used.
        with self.assertRaises(ValueError):
            Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,40)
    
    def test_loanamount_negative(self):
         #Verifies if the Loan Amount raises a Value Error in its mutator with a negative
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(ValueError):
            expected.LoanAmount = -1
    
    def test_loanamount_zero(self):
        #Verifies if the Loan Amount raises a Value Error in its mutator with a 0
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(ValueError):
            expected.LoanAmount = 0
    
    def test_loanamount_positive(self):
        #Verifies that the Loan Amount Accessor returns a positive value
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        expected.LoanAmount = 1
        self.assertEqual(expected.LoanAmount, 1)

    def test_rate_true(self):
        #Verifies that the Rate is one of the possible MortgageRate enums
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        expected.Rate = MortgageRate.FIXED_1
        self.assertEqual(expected.Rate,MortgageRate.FIXED_1)
        
    def test_rate_false(self):
        #Verifies that the Rate is not one of the MortgageRate enums
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(ValueError):
            expected.Rate = ""
        
    def test_freq_true(self):
        #Verifies that the Frequency is one of the MortgageFrequency enums
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        expected.Frequency = MortgageFrequency.BI_WEEKLY
        self.assertEqual(expected.Frequency, MortgageFrequency.BI_WEEKLY)
    
    def test_freq_false(self):
        #Verifies that the Frequency is not one of the MortgageFrequency enums
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(ValueError):
            expected.Frequency = ""
            
    def test_amort_true(self):
        #Verifies that the Amort is one of the VALID_AMORTIZATION values
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        expected.Amortization = 5
        self.assertEqual(expected.Amortization, 5)
    
    def test_amort_false(self):
        #Verifies that the Amort is not one of the VALID_AMORTIZATION values
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)
        with self.assertRaises(Exception):
            expected.Amortization = 1
    
    def test_init(self):
        #A test case to ensure that the __init__ properly sets the attributes when valid inputs are provided.
        expected = Mortgage(1,MortgageRate.FIXED_1,MortgageFrequency.BI_WEEKLY,5)

        self.assertEqual(expected.LoanAmount,1)
        self.assertEqual(expected.Rate,MortgageRate.FIXED_1)
        self.assertEqual(expected.Frequency,MortgageFrequency.BI_WEEKLY)
        self.assertEqual(expected.Amortization,5)
        
    def test_calculate_payment_biweekly(self):
        # Verifies that the payment calculates properly with 2 places and with a Frequency of BiWeekly
        #payment_result = (2 * (0.0579/26 * (1 + 0.0579/26)**(5*26))/((1+0.0579/26)**(5*26) - 1))
        payment_result = 0.02
        expected = Mortgage(2,MortgageRate.FIXED_3,MortgageFrequency.BI_WEEKLY,5)
        actual_payment = expected.calculate_payment()
        self.assertAlmostEqual(actual_payment,payment_result,places=2)
        
    def test_calculate_payment_monthly(self):
        # Verifies that the payment calculates properly with 2 places and with a Frequency of Monthly
        payment_result = 4046.23
        expected = Mortgage(682912.43,MortgageRate.FIXED_1,MortgageFrequency.MONTHLY,30)
        actual_payment = expected.calculate_payment()
        self.assertAlmostEqual(actual_payment,payment_result,places=2)
        
    def test_calculate_payment_weekly(self):
        # Verifies that the payment calculates properly with 2 places and with a Frequency of Weekly
        #payment_result = (10000 * ((0.05/52) * (1 + (0.05/52))**(20*52))/((1 + (0.05/52))**(20*52) - 1))
        payment_result = 15.22
        expected = Mortgage(10000,MortgageRate.FIXED_5,MortgageFrequency.WEEKLY,20)
        actual_payment = expected.calculate_payment()
        self.assertAlmostEqual(actual_payment,payment_result,places=2)
        
    def test_str_monthly(self):
        # Verifies that the mortgage obj string representation is correct with a places of 2 with a Freq of Monthly
        expected = Mortgage(682912.43, MortgageRate.FIXED_1, MortgageFrequency.MONTHLY, 30)
        expected_str = (
            "Mortgage Amount: $682,912.43\n"
            "Rate: 5.89%\n"
            "Amortization: 30\n"
            "Frequency: Monthly -- Calculated Payment: $4,046.23"
        )
        self.assertEqual(str(expected), expected_str)
        
    def test_str_biweekly(self):
        # Verifies that the mortgage obj string representation is correct with a places of 2 with a Freq of BiWeekly
        expected = Mortgage(2, MortgageRate.FIXED_3, MortgageFrequency.BI_WEEKLY, 5)
        expected_str = (
            "Mortgage Amount: $2.00\n"
            "Rate: 5.79%\n"
            "Amortization: 5\n"
            "Frequency: Bi_weekly -- Calculated Payment: $0.02"
        )
        self.assertEqual(str(expected), expected_str)

    def test_str_weekly(self):
        # Verifies that the mortgage obj string representation is correct with a places of 2 with a Freq of Weekly
        expected = Mortgage(10000, MortgageRate.FIXED_5, MortgageFrequency.WEEKLY, 20)
        expected_str = (
            "Mortgage Amount: $10,000.00\n"
            "Rate: 5.00%\n"
            "Amortization: 20\n"
            "Frequency: Weekly -- Calculated Payment: $15.22"
        )
        self.assertEqual(str(expected), expected_str)
        
    def test_repr(self): 
        # Verifies that the mortgage obj representation is correct with proper precision
        expected = Mortgage(682912.43, MortgageRate.FIXED_1, MortgageFrequency.MONTHLY, 30)
        expected_repr = "[682912.43, 0.0589, 30, 12]"
        self.assertEqual(repr(expected),expected_repr)
        

        
#(principal_loan * (interest_rate * (1 + interest_rate)**number_of_payments)/((1+interest_rate)**number_of_payments - 1))
#(2 * (0.0579 * (1 + 0.0579)**5)/((1+0.0579)**5 - 1))
        



if __name__ == '__main__':
    TestCase.main()





